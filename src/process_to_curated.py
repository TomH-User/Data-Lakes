import io
import pandas as pd
import boto3
from transformers import AutoTokenizer


def process_to_curated(bucket_staging, bucket_curated, input_file, output_file, model_name):
    """
    Processes data from the staging bucket, tokenizes sequences, and uploads the processed file to the curated bucket.

    Steps:
    1. Connect to LocalStack S3 using `boto3` and fetch the input file from the staging bucket.
    2. Ensure the input file contains a `sequence` column.
    3. Use a pre-trained tokenizer to tokenize the sequences in the `sequence` column. 
       The right model's name is already passed as a default argument so you shouldn't worry about that.
       In case you are curious, the tokenizer we are using is associted to META's ESM2 8M model, that was state of the art in protein sequence classification some time ago.
       In case you are even more curious, you can try using tokenizers from other models such as ProtBert, but you will likely need to adapt the preprocessing to those tokenizers.
    4. Drop the original sequence field, add a tokenized sequence field to the data
    5. Save the processed data to a temporary file locally.
    6. Upload the processed file to the curated bucket.

    Parameters:
    - bucket_staging (str): Name of the staging S3 bucket.
    - bucket_curated (str): Name of the curated S3 bucket.
    - input_file (str): Name of the file to process in the staging bucket.
    - output_file (str): Name of the output file to store in the curated bucket.
    - model_name (str): Name of the Hugging Face model for tokenization.
    """
    # Step 1: Initialize S3 client
    # HINT: Use boto3.client and specify the endpoint URL to connect to LocalStack.

    # Step 2: Download the input file from the staging bucket
    # HINT: Use s3.get_object to download the file and load it into a Pandas DataFrame.
    # Ensure the input file exists and contains a 'sequence' column.

    # Step 3: Initialize the tokenizer
    # HINT: Use AutoTokenizer.from_pretrained(model_name) to load a tokenizer for the specified model.

    # Step 4: Tokenize the sequences
    # HINT: Iterate over the 'sequence' column and use the tokenizer to process each sequence.
    # Use truncation, padding, and max_length=1024 to prepare uniform tokenized sequences.

    # Step 5: Create a DataFrame for tokenized sequences
    # HINT: Convert the tokenized outputs into a DataFrame. Name the columns as `token_0`, `token_1`, etc.

    # Step 6: Merge the tokenized data with the metadata
    # HINT: Exclude the 'sequence' column from the metadata and concatenate it with the tokenized data.

    # Step 7: Save the processed data locally
    # HINT: Save the final DataFrame to a temporary file using `to_csv`.

    # Step 8: Upload the processed file to the curated bucket
    # HINT: Use s3.upload_fileobj to upload the file from the local path to the S3 curated bucket.


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Process data from staging to curated bucket")
    parser.add_argument("--bucket_staging", type=str, required=True, help="Name of the staging S3 bucket")
    parser.add_argument("--bucket_curated", type=str, required=True, help="Name of the curated S3 bucket")
    parser.add_argument("--input_file", type=str, required=True, help="Name of the input file in the staging bucket")
    parser.add_argument("--output_file", type=str, required=True, help="Name of the output file in the curated bucket")
    parser.add_argument("--model_name", type=str, default="facebook/esm2_t6_8M_UR50D", help="Tokenizer model name")
    args = parser.parse_args()

    process_to_curated(args.bucket_staging, args.bucket_curated, args.input_file, args.output_file, args.model_name)