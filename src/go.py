## INFO ##
## INFO ##

#-- CHEATSHEET ----------------------------------------------------------------#
# HOWTO: http://sublimetext.info/docs/en/reference/syntaxdefs.html
# REGEX: http://manual.macromates.com/en/regular_expressions

# hexadecimal  | octal         | newline   | double-quote |
# single-quote | question-mark | bell      | backspace    |
# formfeed     | line-feed     | return    | tab          |
# vertical-tab | escape char
ESC_CHARS = r'(\\("|\'|\?|a|b|f|n|r|t|v|\\))'
HEX_CHARS = r'(\\x((\h{2})|(\h{,1})))'
UNI_CHARS = r'(\\((u\h{4}|U\h{8})|(u\h{,3}|U\h{,7})))'
OCT_CHARS = r'(\\(([0-7]{3})|([0-7]{,2})))'

# Syntax Definition
syntax = {
    'name': '{NAME}',
    'comment': ('\n\t\tCopyright (C) 2016 Peter Varo'
                '\n\t\t<http://github.com/petervaro/go>'
                '\n'
                '\n\t\tThis program is free software: you can redistribute it'
                '\n\t\tand/or modify it under the terms of the GNU General'
                '\n\t\tPublic License as published by the Free Software'
                '\n\t\tFoundation, either version 3 of the License, or (at your'
                '\n\t\toption) any later version.'
                '\n'
                '\n\t\tThis program is distributed in the hope that it will be'
                '\n\t\tuseful, but WITHOUT ANY WARRANTY; without even the'
                '\n\t\timplied warranty of MERCHANTABILITY or FITNESS FOR A'
                '\n\t\tPARTICULAR PURPOSE. See the GNU General Public License'
                '\n\t\tfor more details.'
                '\n'
                '\n\t\tYou should have received a copy of the GNU General Public'
                '\n\t\tLicense along with this program, most likely a file in'
                '\n\t\tthe root directory, called "LICENSE". If not, see'
                '\n\t\t<http://www.gnu.org/licenses>.'
                '\n\t'),
    'scopeName': 'source.{SCOPE}',
    # Patterns
    'patterns':
    [
        #-- COMMENT -----------------------------------------------------------#
        {
            # One-liner
            'name' : 'comment.line.double_slash.{SCOPE}',
            'match': r'//.*$',
        },
        {
            # Multi-liner
            'name' : 'comment.block.slash_star.{SCOPE}',
            'begin': r'/\*',
            'end'  : r'\*/'
        },

        #-- NUMBERS -----------------------------------------------------------#
        {
            # .001  .1e6  .1E6  .1e+6  .1E+6  .1e-6  .1E-6
            'name' : 'constant.numeric.float_and_complex.decimal.dotted.{SCOPE}',
            'match': r'(?<=\W|^)\.\d+([eE][+-]?\d+)?i?'
        },
        {
            # 1.  1.0  1.e10  1.1e6  1.1E6  1.1e+6  1.1E+6  1.1e-6  1.1E-6
            'name' : 'constant.numeric.float_and_complex.decimal.complete.{SCOPE}',
            'match': r'\d+\.\d*([eE][+-]?\d+)?i?'
        },
        {
            # 1e6 1E6
            'name' : 'constant.numeric.float.decimal.undotted.{SCOPE}',
            'match': r'\d+[eE][+-]?\d+i?'
        },
        {
            # 1i
            'name' : 'constant.numeric.complex.decimal.{SCOPE}',
            'match': r'\d+i'
        },
        {
            'name' : 'constant.numeric.integer.hexadecimal.{SCOPE}',
            'match': r'\b0[xX]\h+'
        },
        {
            'name' : 'constant.numeric.integer.octal.{SCOPE}',
            'match': r'\b0[0-7]+'
        },
        {
            'name' : 'constant.numeric.integer.decimal.{SCOPE}',
            'match': r'\b\d+'
        },

        #-- CONSTANTS ---------------------------------------------------------#
        {
            'include': '#strong_constants',
        },

        #-- MAGIC STUFFS ------------------------------------------------------#
        {
            'include': '#language_variables'
        },

        #-- KEYWORDS ----------------------------------------------------------#
        {
            'name' : 'keyword.storage.specifiers.{SCOPE}',
            'match': r'\b(type|func|var)\b'
        },
        {
            'name' : 'keyword.type.qualifiers.{SCOPE}',
            'match': r'\b(const)\b'
        },
        {
            'name' : 'keyword.control.module.{SCOPE}',
            'match': r'\b(import|package)\b'
        },
        {
            'name' : 'keyword.control.iteration.{SCOPE}',
            'match': r'\b(for|range)\b'
        },
        {
            'name' : 'keyword.control.switch.{SCOPE}',
            'match': r'\b(switch|case|default)\b'
        },
        {
            'name' : 'keyword.control.jumps.{SCOPE}',
            'match': r'\b(break|continue|goto|fallthrough|return)\b'
        },
        {
            'name' : 'keyword.control.conditional.{SCOPE}',
            'match': r'\b(if|else)\b'
        },
        {
            'name' : 'keyword.other.other.{SCOPE}',
            'match': r'\b(chan|defer|go|map|select)\b'
        },

        #-- OPERATORS ---------------------------------------------------------#
        {
            'name' : 'keyword.operator.assignment.augmented.{SCOPE}',
            'match': r'\+\+|--|(\+|-|\*|/|%|&|&?\^|\||<<|>>)='
        },
        {
            'name' : 'keyword.operator.comparison.{SCOPE}',
            'match': r'(<|>)=?|(=|!)='
        },
        {
            'name' : 'keyword.operator.bool.logical.{SCOPE}',
            'match': r'&&|\|\||!'
        },
        {
            'name' : 'keyword.operator.arithmetic.{SCOPE}',
            'match': r'\+|-|\*|/|%|&|&?\^|\||~|<<|>>|'
        },
        {
            'name' : 'keyword.operator.assignment.{SCOPE}',
            'match': r':?='
        },
        {
            'name' : 'keyword.operator.access.{SCOPE}',
            'match': r'\.|:'
        },
        {
            'name' : 'keyword.operator.separator.{SCOPE}',
            'match': r';'
        },
        {
            'name' :'aa' 'keyword.operator.receiver.{SCOPE}',
            'match': r'<-'
        },

        #-- BUILTINS ----------------------------------------------------------#
        {
            'include': '#builtin_types'
        },
        {
            'include': '#builtin_functions'
        },

        #-- ACCESS ------------------------------------------------------------#
        {
            'name' : 'meta.function_call.{SCOPE}',
            'begin': r'([a-zA-Z_]\w*)\s*\(',
            'beginCaptures':
            {
                1: {'name': 'support.function.name.{SCOPE}'}
            },
            'patterns':
            [
                {'include': '$self'}
            ],
            'end':r'\)'
        },
        {
            'name' : 'meta.struct_defintion.{SCOPE}',
            'begin': r'(?<=struct)\s*{',
            'patterns':
            [
                {
                    'include': '$self'
                },
                {
                    'name' : 'variable.struct.member.anonymous.{SCOPE}',
                    'match': r'(?<=^|;)\s*(\**)\s*[a-zA-Z_]\w*(?=\s*(;|$))',
                    'captures':
                    {
                        1: {'name': 'keyword.operator.pointer.{SCOPE}'}
                    }
                },
                {
                    'name' : 'meta.struct.member.anonymous.{SCOPE}',
                    'match': r'(?<=^|;)\s*(\**)?\s*'
                             r'([a-zA-Z_]\w*(\.))+'
                             r'([a-zA-Z_]\w*)(?=\s*(;|$))',
                    'captures':
                    {
                        1: {'name': 'keyword.operator.pointer.{SCOPE}'},
                        3: {'name': 'keyword.operator.separator.{SCOPE}'},
                        4: {'name': 'variable.struct.member.anonymous.{SCOPE}'},

                    }
                },
                {
                    'name' : 'variable.struct.member.anonymous.{SCOPE}',
                    'match': r'(?<=^|[;{])\s*[a-zA-Z_]\w*(?=\s*(;|$))',
                },
                {
                    'name' : 'variable.struct.member.named.{SCOPE}',
                    'match': r'(?<=^|[,;{])\s*[a-zA-Z_]\w*(?=\s+\w|\s*[\[,*])'
                },
            ],
            'end': r'}'
        },
        {
            'name' : 'meta.struct_literal.{SCOPE}',
            'begin': r'{',
            'patterns':
            [
                {
                    'name' : 'variable.language.member_name.{SCOPE}',
                    'match': r'[a-zA-Z_]\w*(?=\s*:(?!=|\s*$))'
                },
                {
                    'include': '$self'
                },
                {
                    'name' : 'meta.exclude.brackets.{SCOPE}',
                    'begin': r'\[',
                    'patterns':
                    [
                        {
                            'include': '$self'
                        }
                    ],
                    'end': r'\]'
                },
            ],
            'end':r'}'
        },
        {
            'name' : 'variable.language.member_access.{SCOPE}',
            'match': r'(?<=\.)[a-z_]\w*'
        },

        #-- STRING ------------------------------------------------------------#
        {
            'include': '#string_quoted'
        },
    ],

    #-- REPOSITORY ------------------------------------------------------------#
    'repository':
    {
        'builtin_types':
        {
            'patterns':
            [
                {
                    'name' : 'support.type.{SCOPE}',
                    'match': r'\b('
                             r'bool|string|u?int(8|16|32|64)?|byte|rune|'
                             r'float(32|64)|complex(64|128)|error|uintptr'
                             r')\b'
                },
                {
                    'name' : 'storage.modifier.variable.type.special.{SCOPE}',
                    'match': r'\b((Complex|Float|Integer)?Type|Type1)\b'
                },
                {
                    'name' : 'support.type.member.{SCOPE}',
                    'match': r'\b(struct|interface)\b'
                }
            ]
        },
        'builtin_functions':
        {
            'patterns':
            [
                {
                    'name' : 'entity.other.function.builtins.{SCOPE}',
                    'match': r'\b('
                             r'append|cap|close|complex|copy|delete|imag|len|'
                             r'make|new|panic|print|println|real|recover'
                             r')\b'
                }
            ]
        },
        'language_variables':
        {
            'patterns':
            [
                {
                    'name' : 'keyword.operator.anonymous.{SCOPE}',
                    'match': r'\b(_)\b'
                },
                {
                    'name' : 'support.type.variable_number.{SCOPE}',
                    'match': r'\.{3}'
                },
            ]
        },
        'strong_constants':
        {
            'name' : 'constant.language.word_like.{SCOPE}',
            'match': r'\b(nil|true|false|iota)\b'
        },
        'string_oct':
        {
            'patterns':
            [
                {
                    'name' : 'invalid.illegal.string.quoted.octal.{SCOPE}',
                    'match': r'\\[0-7]{,2}'
                },
                {
                    'name' : 'constant.character.escaped.octal.{SCOPE}',
                    'match': r'\\[0-7]{3}'
                }
            ]
        },
        'string_hex':
        {
            'patterns':
            [
                {
                    'name' : 'invalid.illegal.string.quoted.hexadecimal.{SCOPE}',
                    'match': r'\\x\h{,1}'
                },
                {
                    'name' : 'constant.character.escaped.hexadecimal.{SCOPE}',
                    'match': r'\\x\h{2}'
                }
            ]
        },
        'string_uni':
        {
            'patterns':
            [
                {
                    'name' : 'invalid.illegal.string.quoted.unicode.{SCOPE}',
                    'match': r'(\\u\h{,3}|\\U\h{,7})'
                },
                {
                    'name' : 'constant.character.escaped.unicode.{SCOPE}',
                    'match': r'(\\u\h{4}|\\U\h{8})'
                }
            ]
        },
        'string_esc':
        {
            'patterns':
            [
                {
                    'name' : 'constant.character.escaped.escape.{SCOPE}',
                    'match': r'\\("|\'|\?|a|b|f|n|r|t|v|\\)'
                },
                {
                    'name' : 'invalid.illegal.string.quoted.escape.{SCOPE}',
                    'match': r'\\.'
                }
            ]
        },
        'string_fmt':
        {
            'name' : 'string.interpolated.format.{SCOPE}',
            'match': r'%(%|((\[\])|\[(((0)|[1-9])\d*)\])?((#|\+)?v|'
                     r'((\d+|\*)\.?(\d+|\*)?|\.(\d+|\*))?f|'
                     r'[bcdeEFgGopqstTxXU]))',
            'captures':
            {
                3: {'name': 'invalid.illegal.interpolated.empty_index.{SCOPE}'},
                4: {'name': 'storage.modifier.interpolated.format.{SCOPE}'},
                6: {'name': 'invalid.illegal.interpolated.bad_index.{SCOPE}'},
            }
        },
        'string_quoted':
        {
            'patterns':
            [
                # Single Quoted String Literal
                {
                    'name' : 'string.quoted.single.escaped.{SCOPE}',
                    'match': r"'" + ESC_CHARS + r"'",
                    'captures':
                    {
                        1: {'name': 'constant.character.escaped.{SCOPE}'},
                        4: {'name': 'invalid.illegal.string.quoted.escaped.{SCOPE}'},
                    }
                },
                {
                    'name' : 'string.quoted.single.hexadecimal.{SCOPE}',
                    'match': r"'" + HEX_CHARS + r"'",
                    'captures':
                    {
                        1: {'name': 'constant.character.escaped.{SCOPE}'},
                        4: {'name': 'invalid.illegal.string.quoted.hexadecimal.{SCOPE}'},
                    }
                },
                {
                    'name' : 'string.quoted.single.escaped.{SCOPE}',
                    'match': r"'" + UNI_CHARS + r"'",
                    'captures':
                    {
                        1: {'name': 'constant.character.escaped.{SCOPE}'},
                        4: {'name': 'invalid.illegal.string.quoted.hexadecimal.{SCOPE}'},
                    }
                },
                {
                    'name' : 'string.quoted.single.octal.{SCOPE}',
                    'match': r"'" + OCT_CHARS + r"'",
                    'captures':
                    {
                        1: {'name': 'constant.character.escaped.{SCOPE}'},
                        4: {'name': 'invalid.illegal.string.quoted.octal.{SCOPE}'},
                    }
                },
                {
                    'name' : 'string.quoted.single.illegal.{SCOPE}',
                    'match': r"'(\\|'|\n)'",
                    'captures':
                    {
                        1: {'name': 'invalid.illegal.string.quoted.single.{SCOPE}'}
                    }
                },
                {
                    'name' : 'string.quoted.single.regular.{SCOPE}',
                    'match': r"'.(.*?)'",
                    'captures':
                    {
                        1: {'name': 'invalid.illegal.string.quoted.more.{SCOPE}'}
                    }
                },

                # Backticked String Literal
                {
                    'name' : 'string.quoted.backtick.regular.{SCOPE}',
                    'begin': r'`',
                    'patterns':
                    [
                        # any
                    ],
                    'end': r'`'
                },

                # Double Quoted String Literal
                {
                    'name' : 'string.quoted.double.regular.{SCOPE}',
                    'begin': r'"',
                    'patterns':
                    [
                        {
                            'name' : 'constant.quoted.double.escaped.{SCOPE}',
                            'match': ESC_CHARS,
                            'captures':
                            {
                                4: {'name': 'invalid.illegal.string.quoted.escaped.{SCOPE}'},
                            }
                        },
                        {
                            'name' : 'constant.quoted.double.hexadecimal.{SCOPE}',
                            'match': HEX_CHARS,
                            'captures':
                            {
                                4: {'name': 'invalid.illegal.string.quoted.hexadecimal.{SCOPE}'},
                            }
                        },
                        {
                            'name' : 'constant.quoted.double.escaped.{SCOPE}',
                            'match': UNI_CHARS,
                            'captures':
                            {
                                4: {'name': 'invalid.illegal.string.quoted.hexadecimal.{SCOPE}'},
                            }
                        },
                        {
                            'name' : 'constant.quoted.double.octal.{SCOPE}',
                            'match': OCT_CHARS,
                            'captures':
                            {
                                4: {'name': 'invalid.illegal.string.quoted.octal.{SCOPE}'},
                            }
                        },
                        {
                            'name' : 'meta.quoted.double.illegal.{SCOPE}',
                            'match': r'(\\|"|\n)',
                            'captures':
                            {
                                1: {'name': 'invalid.illegal.string.quoted.double.{SCOPE}'}
                            }
                        },
                        {
                            'include': '#string_fmt'
                        },
                    ],
                    'end': r'"'
                },
            ]
        },
    },
    'uuid': '18E265C9-70DE-4D0F-ADC7-73DD2618AED8'
}
