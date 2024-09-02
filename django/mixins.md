## Mixins

Mixins are classes that are not supposed to be instantiated but rather they expand another class's functionalities through inheritance. Why would I not instantiate a mixin? It just would not make sense.

For example, let's say our ten videogame characters all need a speak function.

If we code it in for each of them, it would look like this:

```python {"id":"01J6SPM37MZSAQ9C097HFJTZ8Z"}
class Human:
    def speak(self):
        print('I speak')

class Alien:
    def speak(self):
        print('I speak')

class Orc:
    def speak(self):
        print('I speak')

class Elf:
    def speak(self):
        print('I speak')

...
```

But with a mixin, we can just write the function once and reuse it for every character:

```python {"id":"01J6SPPBXJADQJRNFSF79FBF8H"}
class SpeakMixin:
    def speak(self):
        print('I speak')

class Human(SpeakMixin):
    pass

class Alien(SpeakMixin):
    pass

class Orc(SpeakMixin):
    pass

class Elf(SpeakMixin):
    pass

...
```

It would not make sense to have a disembodied voice that says 'I speak' but it would also not make sense to rewrite the same exact piece of code 10 times. And what if we want to add a new speaking character later on? With a mixin class, it's just easier to give them the ability to speak.

NB: Mixins are only special in that you will never instantiate them. Otherwise, they are normal classes.