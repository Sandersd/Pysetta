# Pysetta (Stone)

I'm too lazy to devoute any time to actually learning French so I set out to write a script that will quiz me on a random phrase every time I open a new terminal.

It pulls from a text file in the format question=answer so it can be used for anything that follows that structure.
For French, I thought it would be nice to hear the correct pronunciation as I learned the phrases so I set up text to speech with [Pyvona] (http://zacharybears.com/pyvona/).

Also, I knew I would try to cheat so I handle KeyboardInterrupt exceptions (CTRL-C) but CTRL-\ will still cause Python to quit if needed.

To run on every new window, I just run the script in my config.fish file.
