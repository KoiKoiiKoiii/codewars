using System;
using System.Collections.Generic;

public class DnaStrand
{
    public static string MakeComplement(string dna)
    {
        Dictionary<char, char> myDictionary = new Dictionary<char, char>();

        string result = "";

        myDictionary.Add('A', 'T');
        myDictionary.Add('T', 'A');
        myDictionary.Add('G', 'C');
        myDictionary.Add('C', 'G');

        foreach (var pair in dna)
        {
            result += myDictionary[pair];
        }

        return (result);
    }
}
