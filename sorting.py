def main():
    list = [
            {'post_sort': 'css', 'post_title': 'CSS is Awesome, a zero div infinite zoom animation. Just CSS no JS and no additional HTML', 'post_vote': '161', 'post_link': 'https://www.reddit.com/r/css/comments/i7a89'}, 
            {'post_sort': 'css', 'post_title': 'Dual Bottom Sheets demo, CSS translation and scale transitions to animate synchronized bottom sheets', 'post_vote': '152', 'post_link': 'https://www.reddit.com/r/css/comments/i3sgk'}, 
            {'post_sort': 'css', 'post_title': 'I made Bubble Bobble pixel art with CSS today!', 'post_vote': '127', 'post_link': 'https://www.reddit.com/r/css/comments/i586e9'}, 
            {'post_sort': 'css', 'post_title': 'I animated The Batman title intro in CSS & SVG', 'post_vote': '117', 'post_link': 'https://www.reddit.com/r/css/comments/iio87p'}, 
            {'post_sort': 'css', 'post_title': 'I learnt a new trick tonight - pixel art! One div, styled using box shadows!', 'post_vote': '120', 'post_link': 'https://www.reddit.com/r/css/comments/i4r6if'}, 
            {'post_sort': 'css', 'post_title': 'I animated the Gotham intro in CSS', 'post_vote': '110', 'post_link': 'https://www.reddit.com/r/css/comments/i2xnti'}, 
            {'post_sort': 'golang', 'post_title': 'I also push directly to prod!', 'post_vote': '630', 'post_link': 'https://www.reddit.com/r/golang/comments/i91ynq'}, 
            {'post_sort': 'golang', 'post_title': 'Golang 1.15 released!', 'post_vote': '404', 'post_link': 'https://www.reddit.com/r/golang/comments/i80s89'}, 
            {'post_sort': 'golang', 'post_title': "Let's Fork built with Go and React Native", 'post_vote': '398', 'post_link': 'https://www.reddit.com/r/golang/comments/i5e0t9'}, 
            {'post_sort': 'golang', 'post_title': 'That moment when you catch something on background of a commercial in an airport.', 'post_vote': '326', 'post_link': 'https://www.reddit.com/r/golang/comments/ijgldp'}, 
            {'post_sort': 'golang', 'post_title': 'Generics examples by Go Team 🔥️', 'post_vote': '262', 'post_link': 'https://www.reddit.com/r/golang/comments/iiuhc1'},
            {'post_sort': 'golang', 'post_title': 'How to find a job as a Go developer?', 'post_vote': '247', 'post_link': 'https://www.reddit.com/r/golang/comments/i9ma30'}, 
            {'post_sort': 'flutter', 'post_title': "Where to go after App Brewery's course?", 'post_vote': '65', 'post_link': 'https://www.reddit.com/r/flutter/comments/gcma7d'}, 
            {'post_sort': 'flutter', 'post_title': 'Is Provider Package enough for state management?', 'post_vote': '19', 'post_link': 'https://www.reddit.com/r/flutter/comments/gc9upr'}, 
            {'post_sort': 'flutter', 'post_title': 'Can Flutter export an iOS app that can run on iPhones via sideloading?', 'post_vote': '10', 'post_link': 'https://www.reddit.com/r/flutter/comments/gcl5wa'}, 
            {'post_sort': 'flutter', 'post_title': 'Flutter Music Sample (Android/iOS)', 'post_vote': '13', 'post_link': 'https://www.reddit.com/r/flutter/comments/gcf48v'}, 
            {'post_sort': 'flutter', 'post_title': 'Please visit r/FlutterDev for the main Flutter-related community on Reddit', 'post_vote': '9', 'post_link': 'https://www.reddit.com/r/flutter/comments/gcoe1w'}, 
            {'post_sort': 'rust', 'post_title': 'Rust Memory Container Cheat-sheet, publish on GitHub', 'post_vote': '1.2k', 'post_link': 'https://www.reddit.com/r/rust/comments/idwlqu'}, 
            {'post_sort': 'rust', 'post_title': 'Introducing Bevy: a refreshingly simple data-driven game engine and app framework built in Rust', 'post_vote': '1.2k', 'post_link': 'https://www.reddit.com/r/rust/comments/i7bcwu'}, 
            {'post_sort': 'rust', 'post_title': "Laying the foundation for Rust's future", 'post_vote': '948', 'post_link': 'https://www.reddit.com/r/rust/comments/ic2ky7'}, 
            {'post_sort': 'rust', 'post_title': 'My mother made me a plushie Rustacean 😁🦀', 'post_vote': '829', 'post_link': 'https://www.reddit.com/r/rust/comments/if7ns8'}, 
            {'post_sort': 'rust', 'post_title': 'Almost feels like I am getting code review :) I love rust error messages', 'post_vote': '738', 'post_link': 'https://www.reddit.com/r/rust/comments/ig44dj'}, 
            {'post_sort': 'rust', 'post_title': 'Cranelift can now compile rustc- giving nearly 7x faster compilations than LLVM!', 'post_vote': '683', 'post_link': 'https://www.reddit.com/r/rust/comments/iat25g'}
        ]

# [{'name':'Homer', 'age':39}, {'name':'Bart', 'age':10}]

# newlist = sorted(list_to_be_sorted, key=lambda k: k['name']) 

# https://github.com/azaitsev/millify
        
    
    def convert_str_to_num(num):
        if "k" in num:
            result = float(num.strip("k"))*1000
        else:
            result = int(num)
        return result

    def convert_num_to_str(num):
        num_list = []
        if len(int(num)) == 4:
            num_list.append(str(num))
            if num_list[0][1] == '0'
                result = num_list[0][0]+"k"
            else:
                result = num_list[0][0]+"."+num_list[0][1]+"k"
        return result
             

    # sorted_list = sorted(list, key=lambda k:check_vote_num(k['post_vote']), reverse=True)

    for index, item in enumerate(list):
        item['post_vote'] = check_vote_num(item['post_vote'])

        sorted_list = sorted(list, key=lambda vote:vote['post_vote'], reverse=True)

    for index, item in enumerate(list):    
        print(index, item['post_vote'])
    
        
         
if __name__=="__main__":
    main()