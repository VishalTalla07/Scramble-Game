"""
Additional Test cases
"""

import unittest
from unittest.mock import patch
import problem_6

# class SimpleTestCalcWordScore(unittest.TestCase):
#     def test_basic_word_score(self):
#         result = problem_6.calc_word_score("it", 2)
#         self.assertEqual(result, 52)  
#     def test_no_bonus(self):
#         result = problem_6.calc_word_score("it", 3)
#         self.assertEqual(result, 2)  

# class SimpleTestHandUpdate(unittest.TestCase):
#     def test_basic_hand_update(self):
#         hand = {'a': 1, 'b': 1}
#         new_hand = problem_6.hand_update(hand, "ab")
#         self.assertEqual(new_hand, {})

# class SimpleTestWordIsValid(unittest.TestCase):
#     def test_word_is_valid(self):
#         word_list = ["hello", "it"]
#         hand = {'h': 1, 'e': 1, 'l': 2, 'o': 1}
#         self.assertTrue(problem_6.word_is_valid("hello", hand, word_list))

#     def test_word_not_in_list(self):
#         word_list = ["hello", "it"]
#         hand = {'h': 1, 'e': 1, 'l': 2, 'o': 1}
#         self.assertFalse(problem_6.word_is_valid("world", hand, word_list))

# class SimpleTestStartGame(unittest.TestCase):
#     @patch("builtins.input", side_effect=["e"])  
#     @patch("sys.stdout")  
#     def test_start_game_exit_immediately(self, mock_stdout, mock_input):
#         word_list = ["it"] 
#         problem_6.start_game(word_list)

# if __name__ == "__main__":
#     word_list = ["it", "hello", "world"]
#     print("Testing start_game manually. Enter 'e' when prompted to exit.")
#     problem_6.start_game(word_list)

def test_start_game_exit_immediately():
    print("\nMANUAL TEST CASE 1: Exit immediately")
    print("-----------------------------------")
    print("Instructions:")
    print("1. When prompted, enter 'e'")
    print("Expected Result:")
    print("- The game should exit immediately without errors\n")

    word_list = ["it", "hello"]
    problem_6.start_game(word_list)

    print("If the program exited without errors, Test Case 1 PASSED.\n")


def test_start_game_invalid_then_exit():
    print("\nMANUAL TEST CASE 2: Invalid input, then exit")
    print("-------------------------------------------")
    print("Instructions:")
    print("1. When prompted, enter any invalid letter (example: x)")
    print("2. Observe the error message")
    print("3. Then enter 'e'")
    print("Expected Result:")
    print("- Error message is shown")
    print("- Game exits cleanly after 'e'\n")

    word_list = ["it", "hello"]
    problem_6.start_game(word_list)

    print("If the program showed an error and exited without errors, Test Case 2 PASSED.\n")


if __name__ == "__main__":
    print("RUNNING MANUAL TESTS FOR start_game")
    print("==================================")

    test_start_game_exit_immediately()
    test_start_game_invalid_then_exit()
