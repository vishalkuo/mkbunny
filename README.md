# mkbunny
ASCII Bunny memes are nice, but pretty hard to type out. In an effort to improve that experience, I've created `mkbunny`:

## Installation
This is currently a standalone python3 script with no dependencies. A simple copy and paste or git clone should suffice. 

## Usage
For two simple strings:
```
$ python3 mkbunny.py "My teammate when we play 2v2 Smash and I die within the first minute" "me"

⠀     (\__/) My teammate when we play 2v2
   ⠀  (•ㅅ•)  Smash and I die within the
　＿ノ ヽ ノ＼__ first minute 
 /　`/ ⌒Ｙ⌒ Ｙ　ヽ     
( 　(三ヽ人　/　　|     
|　ﾉ⌒＼ ￣￣ヽ　 ノ    
ヽ＿＿＿＞､＿＿_／ 
　　 ｜( 王 ﾉ〈 (\__/) me
　　 /ﾐ`ー―彡\  (•ㅅ•) 
```

While the bunny formats well for Monospaced terminals, it doesn't do well on iMessage, Whatsapp, etc. A format flag can be specified:
```
$ python3 mkbunny.py "My classmates' side projects" "my side projects" -f imsg

⠀         (\__/) My classmates' side projects
   ⠀  (•ㅅ•)     
　＿ノ ヽ ノ＼  __  
 /　`/ ⌒Ｙ⌒ Ｙ　ヽ     
( 　(三ヽ人　 /　　 |     
|　ﾉ⌒＼ ￣￣ヽ　 ノ    
ヽ＿＿＿＞､＿＿_／ 
　　 ｜( 王 ﾉ〈    (\__/) my side projects
　　 /ﾐ`ー―彡\  (•ㅅ•)  
```

It'll look weird in your terminal but copies beautifully to iMessage. 

Further help can be found at `python3 mkbunny --help`
