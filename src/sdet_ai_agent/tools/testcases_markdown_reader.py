from crewai.tools import tool
import pandas as pd
import io

@tool("Markdown Table Reader")
def testcases_markdown_reader(file_path: str) -> list[dict]:
    """Reads a Markdown table from a file and returns a list of dictionaries.

    Args:
        file_path: The path to the Markdown file.

    Returns:
        A list of dictionaries, where each dictionary represents a row in the table.
        The keys of the dictionaries are the table headers.
        Returns an empty list if no table is found or if an error occurs.

    Raises:
        FileNotFoundError: If the specified file does not exist.
        ValueError: If the file does not contain a valid Markdown table or if there is an error during parsing.
    """

    try:
        with open(file_path, 'r', encoding='utf-8') as f:  # Handle encoding for various characters
            markdown_content = f.read()
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {file_path}")

    try:
        # Find the first Markdown table. This assumes there is only one table in the file.
        table_start = markdown_content.find("|")
        if table_start == -1:
            return []  # No table found

        table_end = markdown_content.find("\n\n", table_start) #find the end of the table
        if table_end == -1:
            table_end = len(markdown_content)

        markdown_table = markdown_content[table_start:table_end]

        # Use pandas to parse the Markdown table
        df = pd.read_csv(io.StringIO(markdown_table), sep='|', header=0, skipinitialspace=True, engine='python')

        # Clean up whitespace from column names and values
        df.columns = df.columns.str.strip()
        df = df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)

        # Convert DataFrame to a list of dictionaries
        table_data = df.to_dict(orient='records')
        return table_data

    except pd.errors.ParserError as e:
        raise ValueError(f"Error parsing Markdown table: {e}")
    except Exception as e:
        raise ValueError(f"An unexpected error occurred: {e}")