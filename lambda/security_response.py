import boto3
import json

sns = boto3.client('sns')

SNS_TOPIC_ARN = 'arn:aws:sns:us-east-1:710353053470:SecurityAlerts'

def lambda_handler(event, context):
    try:
        # Parse the incoming Wazuh alert
        body = json.loads(event.get('body', '{}'))
        
        rule_description = body.get('rule', {}).get('description', 'Unknown alert')
        rule_level = body.get('rule', {}).get('level', 0)
        agent_name = body.get('agent', {}).get('name', 'Unknown agent')
        src_ip = body.get('data', {}).get('srcip', 'Unknown IP')
        timestamp = body.get('timestamp', 'Unknown time')
        
        message = f"""
WAZUH SECURITY ALERT
Agent: {agent_name}
Alert: {rule_description}
Severity Level: {rule_level}
Source IP: {src_ip}
Time: {timestamp}
        """
        
        sns.publish(
            TopicArn=SNS_TOPIC_ARN,
            Message=message,
            Subject='Wazuh Security Alert'
        )
        
        return {
            'statusCode': 200,
            'body': json.dumps('Alert sent successfully')
        }
        
    except Exception as e:
        print(f"Error: {str(e)}")
        return {
            'statusCode': 500,
            'body': json.dumps(f'Error: {str(e)}')
        }
