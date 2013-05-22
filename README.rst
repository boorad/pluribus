====
mapr
====

Having just finished reading the original Google `MapReduce paper`_, I
obviously felt the need to try to implement such a system in Python.

My goals are to implement enough of the functionality described in the
paper to be usable, though I strongly warn against ever using this code
for anything real.

Since one of the goals (see Goals, below) is simplicity from an end-user
standpoint, I am following some of Kenneth Reitz's advice_ and starting
with a readme and documentation.


Examples
========

The canonical word-count example::

    # myjob.py
    from mapr import job


    @job.map_
    def emit_words(key, value):
        # key: document name
        # value: document contents
        for word in value.split():
            yield word, 1


    @job.reduce_
    def sum_occurences(key, values):
        # key: a word
        # values: a list of counts
        return sum(values)


Assuming you're running everything on one host, you can ignore the
network connection information.

Start a **mapr** master::

    $ mapr master

Start a **mapr** worker (or several hundred)::

    $ mapr worker

On the master or on another machine that can talk to the master::

    $ mapr job myjob
    # ... wait
    <results>


Goals
=====

Explicit goals are:

* Simple to use, both as an administrator and end-user.
* Well-documented.
* Robust to worker failure.
* Fast-enough.
* Use only the Python (2.7+) standard library (at least to run).

Explicit non-goals are:

* Be a filesystem.
* Robust to master failure.


.. _MapReduce paper: http://research.google.com/archive/mapreduce.html
.. _advice: http://docs.writethedocs.org/en/2013/conference/talks.html#kenneth-reitz
