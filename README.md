tournament
==========

A Django-based system for tournament management based on Swiss System rules.

Forked from https://github.com/jcdenton/chess-tournament

Requirements
------------

 - Participant model
 - Participant registration form
 - Routine to write data file of participants to legacy format
 - Round model
 - Match model
 - Algorithm to determine participants in each match of the next round given the results of the previous round(s)
 - Algorithm to sort participants from winner to loser
 - Match view to indicate current participants, on-deck participants, and permit posting the results of the current match
 - Sorted participant view
