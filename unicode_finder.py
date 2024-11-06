import unicodedata
# Own Module

version = "0.1.0"

class unicode_char :
    def __init__(self, char: str):
        self.char = char
    
    def character(self) :
        return self.char
    
    def index_char(self, arg) :
        if arg == "d" :
            return ord(self.char)
        elif arg == "h" :
            return "%x"%(ord(self.char))
        else :
            raise TypeError
        
    def name(self) :
        return unicodedata.name(self.char)
    
def col(text : str ,fg : str = None ,bg : str = None) :
    fg_text = ""
    bg_text = ""
    try :
        fg_arg = fg.split(" ")
    except Exception:
        None
    try :
        bg_arg = bg.split(" ")
    except Exception:
        None

    # Background
    try :
        if bg_arg[0] == "rgb" :
            bg_text = f"\N{ESC}[48;2;{str(bg_arg[1])}m"
        elif bg_arg[0] == "256" :
            bg_text = f"\N{ESC}[48;5;{str(bg_arg[1])}m"
    except Exception :
        None
    # Foreground
    try :
        if fg_arg[0] == "rgb" :
            fg_text = f"\N{ESC}[38;2;{str(fg_arg[1])}m"
        elif fg_arg[0] == "256" :
            fg_text = f"\N{ESC}[38;5;{str(fg_arg[1])}m"
    except Exception :
        None
        
    return f"{fg_text}{bg_text}{text}\N{ESC}[0m"

def spacer(String : str, Space : int, Char_Fill : str = None, Direction : bool = None) -> str : # Spacer 4th Version
    if Char_Fill == None :
        Char_Fill = " "
    
    if Direction == None :
        Direction = "l"

    name_len = len(str(String))        # Count how many letter

    if Direction == "l" :
        #  v------------------------------- Total available space
        if Space - name_len < Space :        # If blank space is greater than space
            space = Space - name_len         # Find a space
            box = f"{String}"
            for j in range(space) :
                box = f"{box}{Char_Fill}" # Add a space
        else :
            box = f"{String}{Char_Fill}"
        return box
    elif Direction == "r" :
        #  v------------------------------- Total available space
        if Space - name_len < Space :        # If blank space is greater than space
            space = Space - name_len         # Find a space
            box = f"{String}"
            for j in range(space) :
                box = f"{Char_Fill}{box}" # Add a space
        else :
            box = f"{Char_Fill}{String}"
        return box
    else :
        raise TypeError("Invalid Argument")

# Basic Color Code
col_red = "256 196"
col_orange = "256 208"
col_yellow = "256 226"
col_lime = "256 46"
col_green = "256 28"
col_skyblue = "256 51"
col_midblue = "256 33"
col_blue = "256 21"
col_purple = "256 129"
col_pink = "256 207"
col_grey = "256 8"
col_white = "256 15"
        

# chr_input = input("\nInsert the char : ")
# unicode = unicode_char(chr_input)
# chr_num = ord(chr_input) - 9
# chr_loop = chr_num
# print("\n")
# 
# loop = 0
# for i in range(17) :
#     loop += 1
#     chr_loop += 1
#     chr_hex = hex(chr_loop).split('x')[-1]
#     chr_hex_len = len(chr_hex)
#     # Zero Placement
#     if 4 - chr_hex_len < 4 :
#         space = 4 - chr_hex_len
#         chr_hex_fixed = f"{chr_hex}"
#         for j in range(space) :
#             chr_hex_fixed = f"0{chr_hex_fixed}"
#     else :
#         chr_hex_fixed = f"{chr_hex}"
# 
#     try :
#         text = f"{chr_loop} {chr_hex_fixed} {chr(chr_loop)} | {unicodedata.name(chr(chr_loop))}"
#     except ValueError:
#         text = f"{chr_loop} {chr_hex_fixed}   | NO NAME/CHARACTER"
# 
#     if loop == 9 :
#         print(f"> {text} <")
#     else :
#         print(f"  {text}")

while True :
    print("\nUnicode Character Finder        09 May 2024")
    print("===========================================")
    print("(c) - Search by Character")
    print("(i) - Search by Index Character")
    print("(g) - Character Grid")
    print("\n(a) - About")
    print("(x) - Exit")
    print(f"\nV.{version}")
    print("===========================================")
    main_input = input(">> ")
    if main_input == "c" :
        chr_input = input("\nInsert the char : ")
        try :
            unicode = unicode_char(chr_input)
            chr_num = ord(chr_input) - 9
            chr_loop = chr_num
            print("")
            
            loop = 0
            for i in range(17) :
                loop += 1
                chr_loop += 1
                chr_hex = hex(chr_loop).split('x')[-1]
                chr_hex_len = len(chr_hex)
                # Zero Placement for Hexadecimal
                if 4 - chr_hex_len < 4 :
                    space = 4 - chr_hex_len
                    chr_hex_fixed = f"{chr_hex}"
                    for j in range(space) :
                        chr_hex_fixed = f"0{chr_hex_fixed}"
                else :
                    chr_hex_fixed = f"{chr_hex}"
            
                # Zero Placement for Decimal
                if 6 - len(str(chr_loop)) < 6 :
                    space = 6 - len(str(chr_loop))
                    chr_loop_fixed = f"{chr_loop}"
                    for j in range(space) :
                        chr_loop_fixed = f" {chr_loop_fixed}"
                else :
                    chr_loop_fixed = f"{chr_loop}"

                try :
                    text = f"{col(chr_loop_fixed,fg=col_yellow)} {col(chr_hex_fixed,fg=col_skyblue)} {chr(chr_loop)} {col("|",fg=col_grey)} {unicodedata.name(chr(chr_loop))}"
                except ValueError:
                    text = f"{chr_loop_fixed} {chr_hex_fixed}   | NO NAME/CHARACTER"
                    text = col(text,fg=col_grey)
            
                if loop == 9 :
                    print(f"> {text} <")
                else :
                    print(f"  {text}")
        except Exception :
            print("[Error] Can't Find Character")
        input("\nPress enter key to continue. ")
    elif main_input == "i" :
        chr_input = input("\nInsert the code point : ")
        try :
            unicode = unicode_char(chr_input)
            chr_num = chr(int(chr_input,16))
            chr_loop = ord(chr_num) - 9
            print("")
            
            loop = 0
            for i in range(17) :
                loop += 1
                chr_loop += 1
                chr_hex = hex(chr_loop).split('x')[-1]
                chr_hex_len = len(chr_hex)
                # Zero Placement for Hexadecimal
                if 4 - chr_hex_len < 4 :
                    space = 4 - chr_hex_len
                    chr_hex_fixed = f"{chr_hex}"
                    for j in range(space) :
                        chr_hex_fixed = f"0{chr_hex_fixed}"
                else :
                    chr_hex_fixed = f"{chr_hex}"
            
                # Zero Placement for Decimal
                if 6 - len(str(chr_loop)) < 6 :
                    space = 6 - len(str(chr_loop))
                    chr_loop_fixed = f"{chr_loop}"
                    for j in range(space) :
                        chr_loop_fixed = f" {chr_loop_fixed}"
                else :
                    chr_loop_fixed = f"{chr_loop}"

                try :
                    text = f"{col(chr_loop_fixed,fg=col_yellow)} {col(chr_hex_fixed,fg=col_skyblue)} {chr(chr_loop)} {col("|",fg=col_grey)} {unicodedata.name(chr(chr_loop))}"
                except ValueError:
                    text = f"{chr_loop_fixed} {chr_hex_fixed}   | NO NAME/CHARACTER"
                    text = col(text,fg=col_grey)
            
                if loop == 9 :
                    print(f"> {text} <")
                else :
                    print(f"  {text}")
        except Exception :
            print("[Error] Can't Find Character")
        input("\nPress enter key to continue. ")
    elif main_input == "g" :
        line_s = input("Start Line (Hex) : ")
        line_e = input("End Line (Hex) : ")
        
        line_s = int(line_s,16)
        line_e = int(line_e,16) + 1
        
        print("\n      0  1  2  3  4  5  6  7  8  9  A  B  C  D  E  F\n")
        try :
            for i in range(line_s,line_e) :
                print(f"{spacer(f"{i:X}",4,0,"r")}  ",end="")
                for j in range(16) :
                    if j+(i * 16) < 32 or (j+(i * 16) > 130 and j+(i * 16) < 159) :
                        print(f"   ",end="")
                    else :
                        print(f"{chr(j+(i * 16))}  ",end="")
                print("\n")
        except Exception :
            print("[Error] Invalid Input")
        
        input("\nPress enter key to continue. ")
    elif main_input == "a" :
        print("\nAbout")
        print("===========================================")
        print("Unicode Character Finder        09 May 2024")
        print("Create by Ronnapat Phawaphootanon")
        print(f"\nV.{version}")
        print(f"Unicode Database V.{unicodedata.unidata_version}")
        print("\nA simple CLI UCD Finder")
        print("===========================================")
        input("Press enter key to exit. ")
    elif main_input == "x" :
        print("Bye!!")
        break
    else :
        print("[Error] Invalid Input")
