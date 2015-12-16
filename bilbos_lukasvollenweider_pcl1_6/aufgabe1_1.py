#!/usr/bin/env python
# -*- coding: utf-8 -*-
#PCL I, Übung 6, HS15
#Aufgabe 1.1
#Autor: Bill Bosshard
#Matrikel-Nr.: 12-933-255
#Autor: Lukas Vollenweider
#Matrikel-Nr.: 13-751-888

import codecs

class SACTriple(object):
    """
    Class representing a triple of token, POS, lemma from the Text+Berg corpus.
    
    Attributes:
        word: A unicode string containing the token
        pos: A unicode string containing the part of speech tag
        lemma: A unicode string containing the lemma of the token
        upos: A unicode string containing the universal POS tag for the token.
    """

    def __init__(self, line, pos_dict):
        """
        SACTriple initializer.

        Splits the string passed in and assigns the first part to word, the 
        second to pos, and the third to lemma. Calls _look_up_upos to
        calculate upos.

        Args:
            line: A string in the form "word POS lemma", 
                  separated by any whitespace
            pos_dict: A dictionary of POS:UPOS values.
        Returns:
            An SACTriple instance.

        Examples:
        >>> pos_dict = {}
        >>> with codecs.open('pos2upos.tsv') as pos_tbl:
        ...     for line in pos_tbl:
        ...         l = line.split()
        ...         pos_dict[l[0]] = l[1]
        >>> st = SACTriple(u"hat VAFIN haben", pos_dict)
        >>> st.pos
        u'VAFIN'
        >>> st.lemma
        u'haben'
        >>> st.upos, pos_dict
        u'VERB'
        """

        l = line.split(' ')

        self.word = l[0]
        self.pos = l[1]
        self.lemma = l[2]
        self.pos_dict = pos_dict
        self.upos = self._look_up_upos()

    def __eq__(self, other):
        """
        Two SACTriples are equal when their word, POS and lemma are equal.

        Args:
            other: SACTriple to compare.

        Returns:
            True if all fields of self and other are equal, False if there are
            field mismatches, NotImplemented if other is not an SACTriple.
        
        Examples:
            >>> triple1 = SACTriple(u"machen VVINF machen", pos_dict)
            >>> triple2 = SACTriple(u"hat VAFIN haben", pos_dict)
            >>> triple3 = SACTriple(u"machen VVINF machen", pos_dict)
            >>> not_a_triple = u"hat VAFIN haben"
            >>> triple1 == triple3 
            True
            >>> triple2 == triple3
            False
            >>> triple2 == not_a_triple
            False
        """

        if (type(self).__name__ == "SACTriple" and type(other).__name__ == "SACTriple"):
            if (self.word == other.word and self.pos == other.pos and self.lemma == other.lemma):
                return True
            else:
                return False
        else:
            raise NotImplementedError("One can only compare a SACTriple with another SACTriple")

    def __repr__(self):
        """
        Simple string representation function.

        Returns:
            A unicode string of the form 
            SACTriple(u"word POS lemma UPOS", dict)

            The dict is represented as {pos: upos}.

        Examples:
            >>> triple = SACTriple(u"hat VAFIN haben")
            >>> triple
            SACTriple(u"hat VAFIN haben", {u'VAFIN': u'VERB'})
        """
        
        return "SACTriple(u\"" + self.word + " " + self.pos + " " + self.lemma + "\", {u'" + self.pos + "': u'" + self.upos + "'})"  

    def __str__(self):
        """
        Pretty string representation.

        Returns:
            A string of the form 
            'Word: word, POS: pos, Lemma: lemma, UPOS: upos'

        Examples:
            >>> triple = SACTriple("hat VAFIN haben", pos_dict)
            >>> print triple
            Word: "hat", POS: "VAFIN", Lemma: "haben", UPOS: "VERB"
        """

        return "Word: \"" + self.word + "\", POS: \"" + self.pos + "\", Lemma: \"" + self.lemma + "\"" + "\", UPOS: \"" + self.upos + "\""

    def _look_up_upos(self):
        """
        Looks up POS in self.pos_dict to find the right unified equivalent of
        the POS tag.

        Args:
            pos_dict: a dictionary with german POS tags as keys and unified POS
                      tags as values.

        Returns:
            the UPOS correspondence of the POS tag.
        """
        
        return self.pos_dict[self.pos]