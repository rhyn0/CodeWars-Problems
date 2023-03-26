"""Tribonacci Problem from CodeWars.

6Kyu Kata Training from CodeWars

Try this out at: https://www.codewars.com/kata/556deca17c58da83c00002db
"""
__attempt_date__ = "2022-06-26"

# Standard Library


class TribonacciSequenceError(Exception):
    """Error for when input to Tribonacci is incorrect."""

    def __init__(self, seq_len: int) -> None:
        """Initialize error."""
        super().__init__(
            f"Input Tribonacci sequence is not of length 3, input length is {seq_len}"
        )


def tribonacci(signature: list[int | float], n: int) -> list[int | float]:
    """Compute the brother of the Fibonacci sequence, Tribonacci.

    Uses the previous 3 values to compute the next one.

    Raises:
        ValueError: If signature is not of proper length

    Args:
        signature (List[int]): Starting 3 values
        n (int): Output length of sequence

    Returns:
        List[int]: Tribonacci sequence
    """
    trib_starter_seq_len = 3
    if len(signature) != trib_starter_seq_len:
        raise TribonacciSequenceError(len(signature))

    if n == 0:
        return []

    if n <= trib_starter_seq_len:
        return signature[:n]

    ret_list = list(signature)  # don't edit original
    for i in range(3, n):
        ret_list.append(sum(ret_list[i - 3 : i]))

    return ret_list


class Notes:
    """Notes for improvement.

    - get rid of n checks
        + can summarize as ret_list = signature[:n]
    - change range call to be n - 3, which makes ret_list slice more intuitive
    """
