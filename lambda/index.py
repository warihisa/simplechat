import json
import urllib.request

def lambda_handler(event, context):
    try:
        body = json.loads(event['body'])
        message = body['message']  # 入力メッセージ

        api_url = "https://0406-34-31-210-109.ngrok-free.app/generate"

        headers = {"Content-Type": "application/json"}
        data = json.dumps({"prompt": message}).encode("utf-8")

        req = urllib.request.Request(api_url, data=data, headers=headers)

        with urllib.request.urlopen(req) as res:
            result = json.loads(res.read().decode())

        assistant_response = result.get("generated_text", "[No response]")

        return {
            "statusCode": 200,
            "headers": {
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": "*",
            },
            "body": json.dumps({
                "success": True,
                "response": assistant_response
            })
        }

    except Exception as error:
        return {
            "statusCode": 500,
            "headers": {
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": "*",
            },
            "body": json.dumps({
                "success": False,
                "error": str(error)
            })
        }
