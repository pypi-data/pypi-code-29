import prmt


def should_push(
    dst: str,
    default: str = 'y',
    margin: tuple = (1, 1),
) -> bool:

    return prmt.confirm(
        question=f'Do you want to PUSH package to {dst}?\n',
        default=default,
        margin=margin
    )
