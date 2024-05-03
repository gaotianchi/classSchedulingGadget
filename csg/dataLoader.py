from openpyxl.worksheet.worksheet import Worksheet


def get_template(sheet: Worksheet):
    result: list[list[str | None]] = []
    for row in list(sheet.rows)[1:]:
        row_data = [item.value for item in row][1:]
        result.append(row_data)  # type: ignore
    return result


def get_courses_data(sheet: Worksheet):
    result: dict[str, tuple[int, int]] = {}
    for row in list(sheet.rows)[1:]:
        row_data = [item.value for item in row][1:]
        result.update({row_data[0]: (row_data[1], row_data[2])})  # type: ignore
    return result


def get_duties_data(sheet: Worksheet):
    result: dict[tuple[str, str], set[int]] = {}
    courses_row = [item.value for item in list(sheet.rows)[0][1:]]
    classes_row = [item.value for item in list(sheet.columns)[0][1:]]
    for i, row in enumerate(list(sheet.rows)[1:]):
        class_id: int = classes_row[i]  # type: ignore
        for j, col in enumerate(list(row)[1:]):
            course_name: int = courses_row[j]  # type: ignore
            teacher_name: int = col.value  # type: ignore
            key = (course_name, teacher_name)
            if result.get(key):  # type: ignore
                result[key].add(class_id)  # type: ignore
            else:
                result[key] = set([class_id])  # type: ignore
    return result
