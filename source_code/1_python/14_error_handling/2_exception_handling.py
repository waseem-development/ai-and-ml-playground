# # while True:
# #     try:
# #         number = float(input("Enter a number: "))
# #         print(f"{(10 / number):.2f}")
# #     except:
# #         print("Something went wrong — try again")

# # try/except: Py
# # try/catch: JS




# # while True:
# #     try:
# #         number = int(input("Enter a number: "))
# #         print(f"{(10 / number):.2f}")
# #     except ValueError:
# #         print("That's not a valid number")
# #     except ZeroDivisionError:
# #         print("Can't divide by zero")
# #     except KeyError:
# #         print("This key does not belong to our dict")





    



# # try:
# #     result = 10 / 0 # ZeroDivisionError
# # except ZeroDivisionError as e: # as e: here e is an alias
# #     print(f"Error occurred: {e}")
# #     # Error occurred: division by zero
 



# # try:
# #     number = int(input("Enter a number: "))
# # except ValueError:
# #     print("That's not a valid number")
# # except KeyError:
# #     print("That's not a valid number")
# # except IndexError:
# #     print("That's not a valid number")
# # else:
# #     print(f"Great, you entered {number}\nEverything ran without an error")   # only if NO errors


# try:
#     number = int(input("Enter a number: "))
# except ValueError:
#     print("Invalid number")
# finally:
#     print("This is finally block and it always runs")



# def withdraw(balance, amount):
#     if amount > balance:
#         raise ValueError(f"Insufficient funds. You cannot withdraw {amount} as your balance is {balance}")
#     return balance - amount
 
# # withdraw(100, 500)
# # ValueError: Insufficient funds
 
# try:
#     withdraw(100, 500)
# except ValueError as e:
#     print(f"Transaction failed: {e}")


# raise IndexError("jsg fsfsdfgsdjhf ghsdfhs")



class InsufficientFundsError(Exception):
    pass
 
def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientFundsError(f"Dude you are about to be miskeen go away from my face or I will punch on your nose")
    return balance - amount
 
try:
    withdraw(100, 500)
except InsufficientFundsError as e:
    print(f"Blocked: {e}")   # Blocked: Need 500, have 100