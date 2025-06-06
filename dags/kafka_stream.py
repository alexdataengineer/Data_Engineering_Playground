from datetime import datetime, timedelta
import uuid
import json
import logging
from typing import Dict, Any
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago

# Configure logging
logger = logging.getLogger(__name__)

default_args = {
    'owner': 'Alex',
    'depends_on_past': False,
    'start_date': days_ago(1),
    'email_on_failure': True,
    'email_on_retry': True,
    'retries': 3,
    'retry_delay': timedelta(minutes=5),
}

def get_data() -> Dict[str, Any]:
    """
    Fetch random user data from the API.
    
    Returns:
        Dict[str, Any]: Random user data in JSON format
    """
    try:
        import requests
        response = requests.get('https://randomuser.me/api/')
        response.raise_for_status()  # Raise exception for bad status codes
        return response.json()['results'][0]
    except requests.RequestException as e:
        logger.error(f"Error fetching data: {str(e)}")
        raise

def format_data(res: Dict[str, Any]) -> Dict[str, Any]:
    """
    Format the raw user data into a structured format.
    
    Args:
        res (Dict[str, Any]): Raw user data from the API
        
    Returns:
        Dict[str, Any]: Formatted user data
    """
    try:
        location = res['location']
        return {
            'id': str(uuid.uuid4()),
            'first_name': res['name']['first'],
            'last_name': res['name']['last'],
            'gender': res['gender'],
            'address': f"{str(location['street']['number'])} {location['street']['name']}, "
                      f"{location['city']}, {location['state']}, {location['country']}",
            'post_code': location['postcode'],
            'email': res['email'],
            'username': res['login']['username'],
            'dob': res['dob']['date'],
            'registered_date': res['registered']['date'],
            'phone': res['phone'],
            'picture': res['picture']['medium'],
            'processed_at': datetime.utcnow().isoformat()
        }
    except KeyError as e:
        logger.error(f"Error formatting data: Missing key {str(e)}")
        raise

def stream_data() -> None:
    """
    Main function to fetch and process user data.
    Logs the processed data for monitoring.
    """
    try:
        raw_data = get_data()
        processed_data = format_data(raw_data)
        logger.info(f"Successfully processed user data: {json.dumps(processed_data, indent=2)}")
    except Exception as e:
        logger.error(f"Error in stream_data: {str(e)}")
        raise

with DAG(
    'user_automation',
    default_args=default_args,
    description='DAG to fetch and process random user data',
    schedule_interval='@daily',
    catchup=False,
    tags=['user_data', 'automation']
) as dag:
    
    streaming_task = PythonOperator(
        task_id='streaming_task',
        python_callable=stream_data,
        dag=dag,
        doc_md="""
        ### Task Description
        This task fetches random user data from an API, processes it, and logs the results.
        
        #### Steps:
        1. Fetch data from randomuser.me API
        2. Format the data into a structured format
        3. Log the processed data
        """
    )

get_data()