def array_of_names(names_dict):
    full_names = []
    for first, last in names_dict.items():
        full_name = first.capitalize() + " " + last.capitalize()
        full_names.append(full_name)
    return full_names


# Example usage
persons = {
    "jean": "valjean",
    "grace": "hopper",
    "xavier": "niel",
    "fifi": "brindacier"
}

print(array_of_names(persons))
