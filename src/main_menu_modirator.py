import vlc, time
from PyQt5.QtWidgets import QMessageBox
import time
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

import vlc


channel_categories_listed = False 
series_categories_listed = False 
movies_categories_listed = False 
MAX_VOLUME = 230


def reload_audio_tracks(obj):
    obj.audio_tracks =  get_audio_tracks(obj)
    if obj.audio_tracks == False:
        obj.show_msg("No audio avilable for this video")
        return
    load_audio_tracks(obj)

def show_msg(self, msg):
    box = QMessageBox()
    box.setWhatsThis("OBS")
    msg += '\t'*4
    box.setText(msg)
    box.setIcon(QMessageBox.Information)
    x = box.exec_()

def reload_subtitles(obj):
    obj.subtitles =  get_subtitles(obj)
    if obj.subtitles == False:
        obj.show_msg("No subtitles avilable for this video")
    load_subtitles(obj)

def change_time(obj, value):
    print(f"Value ={value}")
    if obj.cached_type == "movie" or obj.cached_type == "series":
        tot_length = obj.player.get_length()
    else:
        return
    netto = int( (value * tot_length) / 100 )
    if netto < obj.player.get_time():
        obj.time_Slider.setValue(value)
        return

    obj.player.set_time(netto)

def load_audio_tracks(obj):
    obj.comboBox_audio.clear()
    if obj.audio_tracks == 0:
        print("Empty audio list")
        return
    
    current_audio = obj.player.audio_get_track()
    current_audio_index = 0
    # [(-1, b'Disable'), (257, b'Track 1 - [French]')]
    if obj.audio_tracks == False:
        return
    for i in obj.audio_tracks:
        # index of the track 
        print(f"going to add audio {i[1].decode()}")
        obj.comboBox_audio.addItem(i[1].decode())

        # set the current audio track 
        if i[0] == current_audio:
            current_audio = obj.comboBox_audio.currentIndex()
    
    obj.comboBox_audio.setCurrentIndex(current_audio_index)
    
    # set the current audio track
    
    #self.comboBox_audio.setCurrentText(current_audio[1].decode())


def set_audio_track(obj):
    # get selected item
    selected = obj.comboBox_audio.currentText().encode()
    # get its index 
    if obj.audio_tracks == False:
        obj.audio_tracks = get_audio_tracks()
        if obj.audio_tracks == False:
            return
    for i in obj.audio_tracks:
        if selected == i[1]:
            obj.player.audio_set_track(i[0])
            print(f"Set audio track to {selected}")
            return True 
    print("Faild to set audio")
    return False

def set_subtitle(obj):
    # get selected item
    selected = obj.comboBox_subtitles.currentText().encode()
    # get its index 
    if obj.subtitles == False:
        obj.subtitles = obj.get_subtitles()
        if obj.subtitles == False:
            return
    for i in obj.subtitles:
        if selected == i[1]:
            obj.player.video_set_spu(i[0])
            print(f"Set audio track to {selected}")
            return True 
    print("Faild to set audio")
    return False


def load_subtitles(obj):
    # [(-1, b'Disable'), (257, b'Track 1 - [French]')]
    obj.comboBox_subtitles.clear()
    if obj.subtitles == 0:
        print("Empty subtitle list")
        return
    current_subtitle = obj.player.video_get_spu()
    current_subtitle_index = 0
    for i in obj.subtitles:
        # index of the track 
        print(f"going to add sub {i[1].decode()}")
        obj.comboBox_subtitles.addItem(i[1].decode())

        # set current subtitles 
        if i[0] == current_subtitle:
            current_subtitle_index = obj.comboBox_subtitles.currentIndex()
    
    obj.comboBox_subtitles.setCurrentIndex(current_subtitle_index)
    
    # set the current audio track

def get_subtitles(obj):
    avilable_subtitles = obj.player.video_get_spu_description()
    # [(-1, b'Disable'), (257, b'Track 1 - [French]')]
    if len(avilable_subtitles) > 0:
        return avilable_subtitles
    else:
        return False

def get_audio_tracks(obj):
    avilable_tracks = obj.player.audio_get_track_description()
    if len(avilable_tracks) > 0:
        return avilable_tracks
    else:
        return False

def change_volume(obj, value):
    netto = int( (value * MAX_VOLUME) / 100 )
    print(f"Value is {netto}")
    obj.player.audio_set_volume(netto)

def put_start_volume(obj):
    current_volume = obj.player.audio_get_volume()
    #netto * 100 / max
    value = int( (current_volume * 100) / MAX_VOLUME )
    obj.volume_control.setValue(value)

def kill_stream(obj):
    obj.player.stop()

def full_screen_flipflop(obj):
    if obj.player.get_fullscreen():
        #self.player.video_set_scale(0.7)
        obj.player.set_fullscreen(False)
        return 
    #self.player.video_set_scale(0.9)
    obj.player.set_fullscreen(True)

def stop_playing(obj):
    obj.player.pause()

def resume(obj):
    obj.player.play()

def stream(obj):
    # need to get the url first.
    selected = obj.listWidget_2.currentItem().text()
    stream_url = obj.get_url(selected)
    if stream_url != None:
        x = obj.stream_now(stream_url)
        if x != False:
            ##### wait 5 second to handle received frames first.
            time.sleep(4)
            ## get avilavble subtitles 
            obj.subtitles = obj.get_subtitles()
            obj.load_subtitles()
            ## get avilable audio tracks 
            obj.audio_tracks = obj.get_audio_tracks()
            obj.load_audio_tracks()
            obj.player.set_title(555)
            obj.put_start_volume()
            #####
            return
    ########################################### Show msg to say link can not found 
    print("Error, can not parse the selected item and no link found")


def stream_now(obj, url):
    obj.player.set_media(vlc.Media(url))
    obj.player.video_set_scale(0.95)
    obj.player.set_title(555)
    obj.player.play()
    state = obj.player.get_state()
    if state == vlc.State.Ended or state == vlc.State.Error:
        ###################################### Show msg to say channel has no signal now 
        print("No signal for this selected item")
        return False 

    return True

def get_url(obj, selected_item):
        category = obj.cached_category
        myList = None
        if obj.cached_type == "movie":
            myList = obj.movies_categories
        elif obj.cached_type == "series":
            myList = obj.series_categories
        elif obj.cached_type == "channel":
                myList = obj.channels_categories
        if category == None or myList == None:
            return 
        
        for i in myList:
            if i[0] == category:
                for j in i[1]:
                    if j.name == selected_item:
                        print(f"Found, {j.name} , {j.link}")
                        return j.link
        return None


def load_channels(obj):
    category = obj.listWidget_channels.currentItem().text()
    obj.cached_category = category
    obj.cached_type = "channel"
    obj.listWidget_2.clear()
    for i in obj.channels_categories:
        if i[0] == category:
            for channel in i[1]:
                obj.listWidget_2.addItem(channel.name)


def load_movies(obj):
    category = obj.listWidget_movies.currentItem().text()
    obj.cached_category = category
    obj.cached_type = "movie"
    obj.listWidget_2.clear()
    for i in obj.movies_categories:
        if i[0] == category:
            for movie in i[1]:
                obj.listWidget_2.addItem(movie.name)

def load_series(obj):
    category = obj.listWidget_series.currentItem().text()
    obj.cached_category = category
    obj.cached_type = "series"
    obj.listWidget_2.clear()
    for i in obj.series_categories:
        if i[0] == category:
            for series in i[1]:
                obj.listWidget_2.addItem(series.name)

def show_channels_category(obj):
    #self.listWidget.addItem("Hi")
    global channel_categories_listed
    obj.stackedWidget.setCurrentIndex(0)
    if channel_categories_listed : # then we have already listed categories
        return
    for i in obj.channels_categories:
        obj.listWidget_channels.addItem(i[0])
    
    channel_categories_listed = True

def show_series_category(obj):
    global series_categories_listed
    try:
        obj.stackedWidget.setCurrentIndex(2)
    except:
        pass
    if series_categories_listed: # then we have already listed categories
            return
    for i in obj.series_categories:
        obj.listWidget_series.addItem(i[0])
    series_categories_listed = True

def show_movies_category(obj):
    global movies_categories_listed
    obj.stackedWidget.setCurrentIndex(1)
    if movies_categories_listed: # then we have already listed it
            return
    for i in obj.movies_categories:
        obj.listWidget_movies.addItem(i[0])
    movies_categories_listed = True







