# Unicode Magic

This blog post is fingerprinted. If you copy-paste it somewhere that can be indexed I will be able to find it, and prove beyond reasonable doubt that you copied it from me. This blog isn't being served by me, but if it was I could serve a slightly different sentence to each visitor and see what each of them did with the content.

You might think twice about copy-pasting for that next essay huh?

This is possible because of Unicode. You might have heard of it in a story about them adding more emojis or something else equally banal. Essentially it's a way to turn letters into numbers. Unicode is an extension for the ASCII encoding which adds support for more languages. At the time of writing Unicode contains 112,956 characters from almost every language, dead or not, and, of course, emoji.

Here we find our first technique. Many languages have characters that *look* like the English alphabet, but aren't. For example, this is an English 'a'. This is a crylic '0'. Can you tell the difference? Well your computer can. It turns out that there are enough similar characters that you can make a sufficiently long string of text unique.

But it doesn't stop there. Unicode also includes six 'non-displaying' characters which aren't rendered by any font. With this we can encode any information we want in empty space: . You can't see it, but after that colon there's the entire text of the bee movie encoded in base 5. Technically this post is 9519 words long.

It's also how this post is fingerprinted. Each sentence contains a combination of these characters which (almost certainly) has never been written before. These *should* remain if they're copy-pasted.

The simple encoder I wrote uses base 5 and a 'null character' to encode arbitrary bytes. This could be made more efficient by creating a UTF-8 like variable-length encoding but this format is only about 5 times larger when encoded so it's not necessary for encoding short works of literary genius.

You can find the encoder [here](https://github.com/zacps/invis-encoder).
