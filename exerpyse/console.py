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
