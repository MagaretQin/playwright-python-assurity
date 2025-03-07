

def build_url_api(app: str, category: int) -> str:
    """
        Args:
            app: str expect application name ie 'tmsandbox'.
            category: int expect category to check.

        Returns:
            URI sanitized with correct application and category depending on function
        """

    if app.lower() == 'tmsandbox':
        base_url = f"https://api.tmsandbox.co.nz/v1/Categories/{category}/Details.json?catalogue=false"
        return base_url

    else:
        raise ValueError('Please check the parameters in the list')