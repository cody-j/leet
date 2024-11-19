
def justify(words, max_width=16):
    lines = [[]] # [ [ 'word', 'word' ] ]

    cli = 0 # current line index
    cll = 0 # current line total word length

    for word in words:
        if (cll + (len(lines[cli]) - 1) + len(word)) >= max_width:
            n_words = len(lines[cli])
            spaces_needed = max_width - (cll + n_words - 1)
            gaps = n_words - 1
            if gaps == 0:
                print('no gaps!')
                lines[cli][0] += ' '*spaces_needed
            else:

                even_spaces = spaces_needed // gaps
                rema_spaces = spaces_needed % gaps

                for i in range(n_words-1):
                    lines[cli][i] += ' '*(even_spaces+1)
                for i in range(rema_spaces):
                    lines[cli][i] += ' '

            lines[cli] = ''.join(lines[cli])

            lines.append([word])
            cli += 1
            cll = len(word)
        else:
            lines[cli].append(word)
            cll += len(word) # ignore spaces until check
    lines[-1] = ' '.join(lines[-1])
    final_spaces = max_width - (len(lines[-1]))
    lines[-1] = lines[-1] + ' '*final_spaces
    justified = lines
    return justified


if __name__=="__main__":
    justified = justify(["This", "is", "an", "example", "of", "text", "justification."])
    for line in justified:
        print(line)
