
# Library to use
import pandas as pd
import simpleaudio as sa
import wave
import time


#Open Database Spelling a word and save to dataframe
with open('cmudict_new.txt') as f:
    data = [line.split(' ', maxsplit=1) for line in f]
df=pd.DataFrame.from_records(data, columns=['word', 'slice'])

df['word'].replace('\s+', ' ', regex=True, inplace=True) # remove extra whitespace
df['word'].replace('\n',' ', regex=True) # remove \n in text

df['slice'].replace('\s+', ' ', regex=True, inplace=True) # remove extra whitespace
df['slice'].replace('\n',' ', regex=True) # remove \n in text

df=df.astype({'word':'string','slice':'string'}) #change data type for variable word dan slice from object to string

# Fucntion Spelling The Sentences
def word_spell(str):
    spell_list = []
    words = str.split()

    for word in words:
        spell=df[df['word']==word]['slice'].tolist()
        spell_list.append(spell[0])

    return spell_list

val_text = input("Masukan Kalimat(tanpa tanda baca dan special karakter):")


try:
    spell1 = word_spell(val_text.upper())
except:
    print("Ejaan kata tidak sukses!")
    spell1 =""

# Play the sound
for word in spell1:
    characters=word
    #Play sound base on spell per word
    for character in characters.split():
        spellkata=character

        filename = "./diphones-indo/"+spellkata+".wav"
        try:
            wave_read = wave.open(filename, 'rb')
        except:
          continue

        audio_data = wave_read.readframes(wave_read.getnframes())
        num_channels = wave_read.getnchannels()
        bytes_per_sample = wave_read.getsampwidth()
        sample_rate = wave_read.getframerate()
        wave_obj = sa.WaveObject(audio_data, num_channels, bytes_per_sample, sample_rate)
    
        play_object = wave_obj.play()
        time.sleep(0.04)
try:       
    play_object.wait_done()
except:
    print("Tidak Ada Sound!")