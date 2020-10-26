package java_challenges.RepeatedWord;

import org.junit.Test;

import static org.junit.Assert.assertEquals;

public class RepeatedWordTest {
    @Test
    public void testRepeatedWordNoMatch(){
        assertEquals("no match found", RepeatedWord.repeatedWord("there here"));

    }
    @Test
    public void testRepeatedWordOneMatch(){
        assertEquals("there", RepeatedWord.repeatedWord("there here there"));

    }
    @Test
    public void testRepeatedWordOneSentence(){
        assertEquals("a", RepeatedWord.repeatedWord("Once upon a time, there was a brave princess who..."));
    }
    @Test
    public void testRepeatedWordLongSentence(){
        assertEquals("it", RepeatedWord.repeatedWord("It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair, we had everything before us, we had nothing before us, we were all going direct to Heaven, we were all going direct the other way – in short, the period was so far like the present period, that some of its noisiest authorities insisted on its being received, for good or for evil, in the superlative degree of comparison only..."));
    }
    @Test
    public void testRepeatedWordShortSentence() {
        assertEquals("summer", RepeatedWord.repeatedWord("It was a queer, sultry summer, the summer they electrocuted the Rosenbergs, and I didn’t know what I was doing in New York..."));
    }
}
