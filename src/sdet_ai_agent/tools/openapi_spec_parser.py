from crewai.tools import tool
from prance import ResolvingParser
import sys

@tool("OpenAPI Spec Parser")
def openapi_spec_parser(spec_path: str) -> dict:
    """Parses an OpenAPI (Swagger) specification using the Prance library and returns a dictionary containing the parsed data.

    Args:
        spec_path: Path to the OpenAPI specification file (YAML or JSON). Can also be a URL.

    Returns:
        A dictionary containing the parsed information from the OpenAPI spec.

    Raises:
        Exception: If there's an error parsing the specification.
    """
    try:
        print(f"************ Started parsing {spec_path}")
        parser = ResolvingParser(spec_path, backend = 'openapi-spec-validator')
        print(f"************ Finished parsing {spec_path}")
        return parser.specification
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {spec_path}")
    except ValueError as e: # Catch Prance parsing errors
        raise ValueError(f"Invalid OpenAPI specification: {e}")
    except Exception as e:
        print(f"************ An unexpected error occurred during parsing: {e}")
        sys.exit(1)
        #raise Exception(f"An unexpected error occurred during parsing: {e}")