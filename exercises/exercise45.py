"""
Extract repeated blocks of chars from a string
"""
from __future__ import print_function
import re


__all__ = ['char_rep']
__version__ = '0.0.1'
DEBUG = False


def _format_re(bchars, brep):
    'annotated in regexp-like format, repeated block of chars'
    bchars = re.escape(bchars)
    if brep > 1:
        return '(%s){%i}' % (bchars, brep)
    else:
        return bchars

def _format_so(bchars, brep):
    'brep(bchars) format for Stack Overflow: http://stackoverflow.com/questions/28519559/compressing-string-with-repeating-chars'
    return '%i(%s)' % (brep, bchars) if bchars else ''

def char_rep(txt, debug=False, _format=_format_re):
    'return repeated blocks of chars in text with their repeat count'
    output,  lastend = [], 0
    #  Somehow the below regex populates the ?P<chars> with UL
    #  from there the repeat will be populated with ULULUL
    for match in re.finditer(r"""(?ms)(?P<repeat>(?P<chars>.+?)(?:(?P=chars))+)""", txt):
        if debug: print('\n  lastend, txt[lastend:] = ',lastend, repr(txt[lastend:]))
        beginpos, endpos = match.span()
        repeat, chars = match.group('repeat'), match.group('chars')
        if lastend < beginpos:  # Skipped a non-repeated, 'single' block
            output.append(_format(txt[lastend:beginpos], 1))
        output.append(_format(chars, repeat.count(chars)))
        lastend = endpos
        if debug:
            print('  match.span() = ', match.span())
            print("  match.group['repeat'] = ", repeat)
            print("  match.group['chars'] = ", chars)
            print("  repeatcount = ", repeat.count(chars))
            print("  output so far = %r" % ''.join(output))
    output = ''.join(output) + _format(txt[lastend:], 1)
    if debug: print("return %r" % output)
    return output


if __name__ == '__main__':
    for n, txt in enumerate('''
    ULULUL
    LDDLDDLDDLDDLXXLCCLCCLCC
    LDDLDDLDDLDDLXXLCCLCCLCCC
    DDLDDLDDLDDLDDLDDLDDLDDLDDLDDL
    LDDLDDLDDLDDLDDLDDLDDLDDLDDLDD
    LLLLDLLLLDLLLLD
    '''.strip().split(), 1):
        output_re = char_rep(txt, debug=DEBUG, _format=_format_re)
        assert re.match('^%s$' % output_re, txt), "Output is not an RE to match all of input string!"
        output_so = char_rep(txt, debug=DEBUG, _format=_format_so)
        print("String %i: %r\n  re_formatted = %r\n  so_formatted = %r\n"
               % (n, txt, output_re, output_so))


# Read more: from Paddy3118 Go deh!: Find repeated blocks of characters in a string: char_rep(). http://paddy3118.blogspot.com/2015/02/find-repeated-blocks-of-characters-in.html#ixzz68UhTr4if
# Under Creative Commons License: Attribution Non-Commercial No Derivatives
