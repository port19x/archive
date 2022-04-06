# A curses touch typing tutor
import curses


def main(stdscr):

    # Init
    stdscr.clear()  # To clear previous terminal contents
    curses.curs_set(False)  # We will make our own cursor
    width = curses.COLS-1  # Max legal width
    height = curses.LINES-4  # Max height minus score
    score = curses.newwin(3, width, 0, 0)
    score.border()
    text = curses.newwin(height, width, 3, 0)
    text.border()
    lesson = "Long live the King!"  # Placeholder
    text.addstr(1, 1, lesson)
    stdscr.refresh()  # Render inital screen
    passed, errors = "", 0
    wcount = len(lesson.split(" "))
    ccount = len(lesson)
    for i in range(ccount):

        # Text
        text.addstr(1, 1, passed, curses.A_BOLD)
        text.addch(1, len(passed)+1, lesson[len(passed)], curses.A_REVERSE)
        text.refresh()

        # Score
        cprogress = "c: {}/{} ".format(i, ccount)
        wpass = len(passed.split(" ")) - errors - 1
        wprogress = "w: {}/{} ".format(wpass, wcount)
        errorstat = "e: {} ".format(errors)
        scorestring = cprogress + wprogress + errorstat
        score.addstr(1, 1, scorestring)
        score.refresh()

        # Input
        keypress = stdscr.getch()
        if keypress == ord(lesson[i]):
            passed += lesson[i]
        else:
            passed += " "
            errors += 1


if __name__ == "__main__":
    curses.wrapper(main)
