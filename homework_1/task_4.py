PATTERN = 'banana'


def bananas(s) -> set:
    def _bananas(
            __edited_string: str,
            __char_number: int,
            __form_char_number: int
    ) -> None:

        if __char_number == count_string:
            if __form_char_number == count_form:
                result.add(__edited_string)
                return
            return
        else:
            _bananas(
                __edited_string + '-',
                __char_number + 1,
                __form_char_number
            )
            if (__form_char_number != count_form
                    and s[__char_number] == PATTERN[__form_char_number]):
                _bananas(
                    __edited_string + PATTERN[__form_char_number],
                    __char_number + 1,
                    __form_char_number + 1
                )

    result = set()
    count_string = len(s)
    count_form = len(PATTERN)
    _bananas('', 0, 0)
    return result


if __name__ == "__main__":
    assert bananas("banann") == set()
    assert bananas("banana") == {
        "banana"
    }
    assert bananas("bbananana") == {
        "b-an--ana", "-banana--", "-b--anana", "b-a--nana", "-banan--a",
        "b-ana--na", "b---anana", "-bana--na", "-ba--nana", "b-anan--a",
        "-ban--ana", "b-anana--"
    }
    assert bananas("bananaaa") == {
        "banan-a-", "banana--", "banan--a"
    }
    assert bananas("bananana") == {
        "ban--ana", "ba--nana", "bana--na", "b--anana", "banana--", "banan--a"
    }
