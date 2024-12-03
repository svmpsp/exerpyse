class ConsolePrinter:
    def print_greeting(self):
        print("📚🐍 Welcome to Exerpyse\n")
        print("Your journey into programming begins here!\n")

    def print_setup(self):
        print("Before we begin, we need to set up a few things first.\n")
        print("* creating exercise directory...")
        print("* copying exercise files...\n")
        print("All done, we are ready to start!")

    def print_reset(self):
        print("Resetting all exercises.\n")
        print("* deleting exercise folder`...")
        print("* creating exercise directory...")
        print("* copying exercise files...\n")
        print("All done, we are ready to start!")

    def check_reset(self) -> bool:
        print(
            "This action will overwrite all your work and "
            "restore the exercises to their initial state.\n"
        )
        answer = input("Are you sure you want to continue (y/N)? ")
        answer = answer.lower().strip()
        if answer in ("yes", "y"):
            print()
            return True
        print("You did not confirm the operation. Type 'yes' to confirm.")
        return False

    def start_exercise(self, path):
        print(f"{path.name} - Checking your work...")

    def end_exercise(self, path):
        print(f"{path.name} - All good, great job!\n")

    def abort_exercise(self, path):
        print(f"Fix the code in exerpyses/{path.name} and try again :)")

    def print_end(self):
        print("🎉🎉🎉 CONGRATULATIONS!!! 🎉🎉🎉\n")
        print("You have successfully completed all of our exercises.")
        print("This means you now know how to write simple programs in Python.\n")
        print("If you are interested and want to learn more, check out these free online resources:")
        print("* TBD.\n")
        print("That's all, and good luck to you on your Programming journey!\n")
        print("The Exerpyse Development Team 📚🐍")