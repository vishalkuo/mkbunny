import sys
import argparse

STR = """
⠀     (\\__/) {0}
   ⠀  (•ㅅ•)  {1}
　＿ノ ヽ ノ＼__ {2} 
 /　`/ ⌒Ｙ⌒ Ｙ　ヽ     
( 　(三ヽ人　/　　|     
|　ﾉ⌒＼ ￣￣ヽ　 ノ    
ヽ＿＿＿＞､＿＿_／ 
　　 ｜( 王 ﾉ〈 (\\__/) {3}
　　 /ﾐ`ー―彡\\  (•ㅅ•) """

I_MSG_STR = """
⠀         (\\__/) {0}
   ⠀  (•ㅅ•)     {1}
　＿ノ ヽ ノ＼  __  {2}
 /　`/ ⌒Ｙ⌒ Ｙ　ヽ     
( 　(三ヽ人　 /　　 |     
|　ﾉ⌒＼ ￣￣ヽ　 ノ    
ヽ＿＿＿＞､＿＿_／ 
　　 ｜( 王 ﾉ〈    (\\__/) {3}
　　 /ﾐ`ー―彡\\  (•ㅅ•)  """


def _split_by_lspace(s, length):
    if len(s) > length:
        last_space = s[:length].rfind(" ")
        if last_space > 0:
            return s[:last_space], s[last_space + 1 :]
        else:
            return "", s
    else:
        return s, ""


def main():
    parser = argparse.ArgumentParser(description="Make a bunny")
    parser.add_argument("big_str", metavar="B", type=str, help="The big bunny text")
    parser.add_argument("small_str", metavar="S", type=str, help="The small bunny text")
    parser.add_argument(
        "-l",
        "--line_length",
        nargs="?",
        type=int,
        default=30,
        help="The line wrap length for big bunny",
    )
    parser.add_argument(
        "-f",
        "--format",
        nargs="?",
        type=str,
        default="mono",
        choices=["mono", "imsg"],
        help="How to format the bunny for pasting",
    )
    args = parser.parse_args()

    big_str = args.big_str
    small_str = args.small_str
    llength = args.line_length
    fmt = args.format
    bs1, bs2, bs3 = "", "", ""
    bs1, bs2 = _split_by_lspace(big_str, llength)
    bs2, bs3 = _split_by_lspace(bs2, llength)

    if fmt == "mono":
        print(STR.format(bs1, bs2, bs3, small_str))
    elif fmt == "imsg":
        print(I_MSG_STR.format(bs1, bs2, bs3, small_str))


if __name__ == "__main__":
    main()
