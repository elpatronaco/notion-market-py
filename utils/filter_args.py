class FilterArgs:
    @staticmethod
    def text_eq(title: str, value: str):
        return {
            "property": title,
            "text": {
                "equals": value
            }
        }

    @staticmethod
    def text_contains(title: str, value: str):
        return {
            "property": title,
            "text": {
                "contains": value
            }
        }

    @staticmethod
    def select_eq(title: str, value: str):
        return {
            "property": title,
            "select": {
                "equals": value
            }
        }

    @staticmethod
    def multi_select_contains(title: str, value: str):
        return {
            "property": title,
            "multi_select": {
                "contains": value
            }
        }