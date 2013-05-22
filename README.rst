====
mapr
====

.. note::

   This falls into the Stupid Programming Tricks series and should not
   be used in production by anything at all.


Examples
========

The canonical word-count example::

    # myjob.py
    from mapr import job


    @job.map_
    def emit_words(text):
        for word in text.split():
            yield word, 1


    @job.reduce_
    def sum_occurences(key, values):
        return sum(values)


Start a **mapr** master::

    $ mapr master -b 192.168.2.1 -p 7787

Start a **mapr** worker (or several hundred)::

    $ mapr worker --master=192.168.2.1:7787

On the master or on another machine that can talk to the master::

    $ mapr job --master=192.168.2.1:7787 myjob.py /path/to/input/
    # ... wait
    <results>
