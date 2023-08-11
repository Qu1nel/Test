#include "wc.h"

#include <stdbool.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

static int32_t parse_options(int32_t key, char *argument, ArgumentParserState *state);
static void check_mode(Arguments **args, Mode setmode);

ArgsOption options[] = {
    {0, 0, 0, 0, "Program output control options:", 1},
    {"bytes", 'c', 0, 0, "Print the byte counts", 0},
    {"words", 'w', 0, 0, "Print the word counts", 0},
    {"lines", 'l', 0, 0, "Print the newline counts", 0},
    {"max-line-length", 'L', 0, 0, "Print the maximum display  width", 0},
    {0, 0, 0, 0, "Informational Options:", -1},
    {0},
};


int main(int argc, char *argv[])
{
    Arguments arguments = {0, {NULL, 0}};
    Argp argp = {options, parse_options, args_doc, doc, 0, 0, 0};

    if (argp_parse(&argp, argc, argv, 0, 0, &arguments) == 0) {
        Counting total_result = {0, 0, 0, 0};

        if (arguments.mode == 0) {
            arguments.mode = PRI_LWB;
        }

        if (arguments.files.name != NULL) {
            const char *prev = NULL;
            char *file_name;

            size_t count_files = 0;

            while ((file_name = argz_next(arguments.files.name, arguments.files.count, prev))) {
                printf("%s\n", file_name);
                prev = file_name;
                count_files++;
            }

            free(arguments.files.name);
        } else {
            // STDOUT
        }
    }

    return EXIT_SUCCESS;
}


static int32_t parse_options(int32_t key, char *argument, ArgumentParserState *state)
{
    Arguments *arguments = (Arguments *)state->input;
    switch (key) {
        case 'l':
            check_mode(&arguments, PRI_NEWLINES);
            break;
        case 'w':
            check_mode(&arguments, PRI_WORDS);
            break;
        case 'c':
            check_mode(&arguments, PRI_BYTES);
            break;
        case 'L':
            check_mode(&arguments, PRI_MAX_LINE_LENGTH);
            break;
        case ARGP_KEY_INIT:
            arguments->files.name = NULL;
            arguments->files.count = 0;
            break;
        case ARGP_KEY_ARG:
            argz_add(&arguments->files.name, &arguments->files.count, argument);
            break;
        default:
            return ARGP_ERR_UNKNOWN;
    }
    return 0;
}

static void check_mode(Arguments **args, Mode setmode)
{
    if ((*args)->mode == NO_INIT) {
        (*args)->mode = (uint16_t)setmode;
    } else {
        (*args)->mode |= (uint16_t)setmode;
    }
}
