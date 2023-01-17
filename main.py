import sys 
import os 
current_dir = os.path.dirname(os.path.abspath(__file__))
current_dir += "\\src"
print(current_dir)
sys.path.insert(1, current_dir)
import main_menu

if __name__ == "__main__":
    main_menu.launch_app()
    print("App Terminates")