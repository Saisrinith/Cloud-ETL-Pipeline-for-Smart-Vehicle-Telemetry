import json
import logging

async def main(context, myBlob):
    logging.info("Processing blob: %s", context.binding_data['blobTrigger']) # More informative logging

    try:
        blob_content = myBlob.decode('utf-8')  # Decode once for efficiency
        json.loads(blob_content.strip().replace('\n', ' ')) # Parse JSON

        context.bindings['stagingFolder'] = blob_content
        logging.info("File copied to staging folder successfully")

    except (UnicodeDecodeError, json.JSONDecodeError) as e: # Catch specific errors
        logging.error("Error processing blob: %s", e)
        context.bindings['rejectedFolder'] = myBlob.decode('utf-8') # Original blob on failure
        logging.info("Invalid file copied to rejected folder")