from ranger import MAX_RESTORABLE_TABS
from ranger.api.commands import Command
# from plugins.ranger_udisk_menu.mounter import mount
from PIL import Image, ImageEnhance, ImageDraw, ImageFont

class paste_as_root(Command):
	def execute(self):
		if self.fm.do_cut:
			self.fm.execute_console('shell sudo mv %c .')
		else:
			self.fm.execute_console('shell sudo cp -r %c .')

class fzf_select(Command):
    """
    :fzf_select

    Find a file using fzf.

    With a prefix argument select only directories.

    See: https://github.com/junegunn/fzf
    """
    def execute(self):
        import subprocess
        import os.path
        if self.quantifier:
            # match only directories
            command="find -L . ( -path '*/.*' -o -fstype 'dev' -o -fstype 'proc' ) -prune \
            -o -type d -print 2> /dev/null | sed 1d | cut -b3- | fzf +m --reverse --header='Jump to file'"
        else:
            # match files and directories
            # command="find -L . \( -path '*/\.*' -o -fstype 'dev' -o -fstype 'proc' \) -prune \
            # -o -print 2> /dev/null | sed 1d | cut -b3- | fzf +m --reverse --header='Jump to filemap <C-f> fzf_select'"
            command="find -L . ( -path '*/.*' -o -fstype 'dev' -o -fstype 'proc' ) -prune \
            -o -print 2> /dev/null | sed 1d | cut -b3- | fzf +m --reverse --header='Jump to filemap <C-f> fzf_select'"
        fzf = self.fm.execute_command(command, universal_newlines=True, stdout=subprocess.PIPE)
        stdout, stderr = fzf.communicate()
        if fzf.returncode == 0:
            fzf_file = os.path.abspath(stdout.rstrip('\n'))
            if os.path.isdir(fzf_file):
                self.fm.cd(fzf_file)
            else:
                self.fm.select_file(fzf_file)

import os
from ranger.core.loader import CommandLoader
class extract_here(Command):
    def execute(self):
        """ extract selected files to current directory."""
        cwd = self.fm.thisdir
        marked_files = tuple(cwd.get_selection())

        def refresh(_):
            cwd = self.fm.get_directory(original_path)
            cwd.load_content()

        one_file = marked_files[0]
        cwd = self.fm.thisdir
        original_path = cwd.path
        au_flags = ['-x', cwd.path]
        au_flags += self.line.split()[1:]
        au_flags += ['-e']

        self.fm.copy_buffer.clear()
        self.fm.cut_buffer = False
        if len(marked_files) == 1:
            descr = "extracting: " + os.path.basename(one_file.path)
        else:
            descr = "extracting files from: " + os.path.basename(
                one_file.dirname)
        obj = CommandLoader(args=['aunpack'] + au_flags
                            + [f.path for f in marked_files], descr=descr,
                            read=True)

        obj.signal_bind('after', refresh)
        self.fm.loader.add(obj)

from ranger.core.loader import CommandLoader

class compress(Command):
    def execute(self):
        """ Compress marked files to current directory """
        cwd = self.fm.thisdir
        marked_files = cwd.get_selection()

        if not marked_files:
            return

        def refresh(_):
            cwd = self.fm.get_directory(original_path)
            cwd.load_content()

        original_path = cwd.path
        parts = self.line.split()
        au_flags = parts[1:]

        descr = "compressing files in: " + os.path.basename(parts[1])
        obj = CommandLoader(args=['apack'] + au_flags + \
                [os.path.relpath(f.path, cwd.path) for f in marked_files], descr=descr, read=True)

        obj.signal_bind('after', refresh)
        self.fm.loader.add(obj)

    def tab(self, tabnum):
        """ Complete with current folder name """

        extension = ['.zip', '.tar.gz', '.rar', '.7z']
        return ['compress ' + os.path.basename(self.fm.thisdir.path) + ext for ext in extension]

class flip_horizontally_old(Command):
    """
    :flip_horizontally

    Flip current video horizontally.
    """
    def execute(self):
        import subprocess
        this_file = self.fm.thisfile
        command="ffmpeg -i " + this_file.path + "  -vf hflip -c:a copy flipped.mp4"

        self.fm.execute_command(command, universal_newlines=True, stdout=subprocess.PIPE)

class flip_horizontally(Command):
    """
    :flip_horizontally2

    Flip current video horizontally2.
    """
    def execute(self):
        import subprocess
        this_file = self.fm.thisfile
        # OLD:
        # ---------------------------------------------------
        # command="ffmpeg -i " + this_file.path + "  -vf hflip -c:a copy "+ this_file.path+"_flipped.mp4"
        # command=f"ffmpeg -i {this_file.path} -vf hflip -c:a copy {this_file.basename_without_extension}_flipped.mp4 && rm {this_file.path}"
        # command=f"echo {self.fm.thistab.get_selection}"
        # ---------------------------------------------------

        for item in self.fm.thistab.get_selection(): 
            # item = /home/chalius/projects/videos/fight-videos-project/videos_created/original_videos/temp/Do_It_-Topstreetfights.com_flipped.mp4

            # Extracting basenam without extension:
            basename = item.path[item.path.rfind("/")+1:]
            without_extension = basename[:basename.rfind(".")]
            # ---------------------------------------------------
            command=f"ffmpeg -i {item.path} -vf hflip -c:a copy {without_extension}_flipped.mp4 && rm {item.path}"
            self.fm.run(command)
            # self.fm.execute_command(command, universal_newlines=True, stdout=subprocess.PIPE)
        

from pymediainfo import MediaInfo
def get_times(path):
    media_info = MediaInfo.parse(path)
    times_array = []
    for track in media_info.tracks:
        if track.track_type == "Video":
            seconds = track.duration / 1000
            time1 = round(seconds * 0.1)
            time2 = round(seconds * 0.3)
            time3 = round(seconds * 0.7)
            time4 = round(seconds * 0.9)
            times_array = [time1, time2, time3, time4]
            return times_array
        elif track.track_type == "Audio":
            print("Track data:")
            # pprint(track.to_data())
            raise Exception("File path isn't a video.")
    return times_array

def make_one_screenshot(seconds, path, output):
    '''Create the screenshot.'''
    # Example:
    # cmd = f"ffmpeg -ss 10 -i {path} -frames 1 screenshot.png"
    cmd = f"ffmpeg -ss {seconds} -i {path} -frames 1 {output}"
    os.system(cmd)

def make_collage(images_array, output_folder, video_name):
    print(images_array)
    print(output_folder)
    print(video_name)

    # images_array:
    # ['./functions/screenshot/temp/4.png', './functions/screenshot/temp/11.png', './functions/screenshot/temp/26.png', './functions/screenshot/temp/34.png']

    new_image = Image.new("RGBA", (2000,2000))

    # img = Image.open("Desktop/300.jpg")
    img1 = Image.open(images_array[0])
    img2 = Image.open(images_array[1])
    img3 = Image.open(images_array[2])
    img4 = Image.open(images_array[3])

    img1 = img1.resize((1000,1000))
    img2 = img2.resize((1000,1000))
    img3 = img3.resize((1000,1000))
    img4 = img4.resize((1000,1000))

    new_image.paste(img1, (0,0))
    new_image.paste(img2, (1000,0))
    new_image.paste(img3, (0,1000))
    new_image.paste(img4, (1000,1000))

    # new.show()
    # output = new_image.save("./output.png")
    output = new_image.save(f"{output_folder}{video_name}.png")

import shutil
class make_screenshots(Command):
    """
    :make_screenshots

    This command makes screenshots of the videos from the current folder.
    """
    def execute(self):
        for item in self.fm.thistab.get_selection(): 
            video_path = item.path

            # Take pictures:
            # ---------------------------------------------------
            times = get_times(video_path)
            images_array = []

            # temp_folder = "./functions/screenshot/temp/"
            temp_folder = f"{item.dirname}/temp/"
            if not os.path.exists(temp_folder): os.makedirs(temp_folder)

            for time in times:
                # temp_output = f"./screenshots/temp/{time}.png"
                temp_output = f"{temp_folder}{time}.png"
                make_one_screenshot(time, video_path, temp_output)
                images_array.append(temp_output)

            # ---------------------------------------------------

            # Make collage:
            # ---------------------------------------------------
            # Extract name from video_path
            arr_path = video_path.split("/")
            video_name = arr_path[len(arr_path)-1]
            # ------------------------

            out_folder = "./output/"
            collages_folder = out_folder
            if not os.path.exists(collages_folder): os.makedirs(collages_folder)
            make_collage(images_array, collages_folder, video_name)

            shutil.rmtree(temp_folder)
            # ---------------------------------------------------


# class test(Command):
#     """
#     :test

#     Test command.
#     """
#     def execute(self):
#         import subprocess
#         # this_file = self.fm.thisfile
#         command=f"echo {Command}"

#         self.fm.execute_command(command, universal_newlines=True, stdout=subprocess.PIPE)

class echo(Command):
    """:echo <text>

    Display the text in the statusbar.
    """

    def execute(self):
        self.fm.notify(self.rest(1))


class reduce_video_size(Command):
    # Note: I must press enter after run the command in order to watch again ranger interface.

    def loop_through_all_files(self):
        # import subprocess
        for index, file in enumerate(self.fm.thistab.get_selection(), start=0): 
            name_without_extension, _ = os.path.splitext(f"{file.basename}")

            command = f"ffmpeg -i {file.dirname}/'{file.basename}' -vcodec libx265 -crf 28 '{name_without_extension}_reduced.mp4'"
            # note: I shoudn't use & at the end, because this creates a new thread and the ring sound isn't work well.
            command += " > /dev/null 2>&1" # send the output to /dev/null

            #process1 = subprocess.Popen(command, shell=True) # detached way
            #self.fm.execute_command(command, universal_newlines=True, stdout=subprocess.PIPE) # chatgpt said that the 2nd and 3rd parameters are innecesary and cand make problems
            self.fm.execute_command(command)


    def ring_sound(self, t1):
        t1.join()
        import subprocess
        end_sound = "paplay /usr/share/sounds/freedesktop/stereo/complete.oga"
        #process2 = subprocess.Popen(end_sound, shell=True) # detached way
        self.fm.execute_command(end_sound, universal_newlines=True, stdout=subprocess.PIPE)


    def execute(self):
        from ranger.core.loader import Loader
        import threading
        t1 = threading.Thread(target=self.loop_through_all_files)
        t1.daemon = True
        t2 = threading.Thread(target=self.ring_sound, args=(t1,))
        t1.start()
        t2.start()

class reduce_image_size(Command):
    # Note: I must press enter after run the command in order to watch again ranger interface.

    def loop_through_all_files(self):
        # import subprocess
        for index, file in enumerate(self.fm.thistab.get_selection(), start=0): 
            name_without_extension, _ = os.path.splitext(f"{file.basename}")

            # command = f"convert {file.dirname}/'{file.basename}' -quality 35% '{name_without_extension}_reduced.jpg'"
            command = f"convert {file.dirname}/'{file.basename}' -quality 50% '{name_without_extension}_reduced.jpg'"
            # note: I shoudn't use & at the end, because this creates a new thread and the ring sound isn't work well.
            command += " > /dev/null 2>&1" # send the output to /dev/null

            #process1 = subprocess.Popen(command, shell=True) # detached way
            #self.fm.execute_command(command, universal_newlines=True, stdout=subprocess.PIPE) # chatgpt said that the 2nd and 3rd parameters are innecesary and cand make problems
            self.fm.execute_command(command)


    def ring_sound(self, t1):
        t1.join()
        import subprocess
        end_sound = "paplay /usr/share/sounds/freedesktop/stereo/complete.oga"
        #process2 = subprocess.Popen(end_sound, shell=True) # detached way
        self.fm.execute_command(end_sound, universal_newlines=True, stdout=subprocess.PIPE)


    def execute(self):
        from ranger.core.loader import Loader
        import threading
        t1 = threading.Thread(target=self.loop_through_all_files)
        t1.daemon = True
        t2 = threading.Thread(target=self.ring_sound, args=(t1,))
        t1.start()
        t2.start()


class extract_audio(Command):
    # Note: I must press enter after run the command in order to watch again ranger interface.

    def loop_through_all_files(self):
        # import subprocess
        for index, file in enumerate(self.fm.thistab.get_selection(), start=0): 
            name_without_extension, _ = os.path.splitext(f"{file.basename}")

            command = f"ffmpeg -i {file.dirname}/'{file.basename}' -acodec libmp3lame '{name_without_extension}_audio.mp3'"

#     #    command = f"ffmpeg -i {this_file.dirname}/'{this_file.basename}' -acodec libmp3lame {this_file.dirname}/'{this_file.basename}.mp3' &"

            # note: I shoudn't use & at the end, because this creates a new thread and the ring sound isn't work well.
            command += " > /dev/null 2>&1" # send the output to /dev/null

            #process1 = subprocess.Popen(command, shell=True) # detached way
            #self.fm.execute_command(command, universal_newlines=True, stdout=subprocess.PIPE) # chatgpt said that the 2nd and 3rd parameters are innecesary and cand make problems
            self.fm.execute_command(command)


    def ring_sound(self, t1):
        t1.join()
        import subprocess
        end_sound = "paplay /usr/share/sounds/freedesktop/stereo/complete.oga"
        #process2 = subprocess.Popen(end_sound, shell=True) # detached way
        self.fm.execute_command(end_sound, universal_newlines=True, stdout=subprocess.PIPE)


    def execute(self):
        from ranger.core.loader import Loader
        import threading
        t1 = threading.Thread(target=self.loop_through_all_files)
        t1.daemon = True
        t2 = threading.Thread(target=self.ring_sound, args=(t1,))
        t1.start()
        t2.start()

class place_file_inside_folder(Command):
    # Note: I must press enter after run the command in order to watch again ranger interface.

    def loop_through_all_files(self):
        import subprocess
        for index, file in enumerate(self.fm.thistab.get_selection(), start=0): 
            name_without_extension, _ = os.path.splitext(f"{file.basename}")

            command = f"mkdir {name_without_extension} && mv {file.basename} '{name_without_extension}'"
            # note: I shoudn't use & at the end, because this creates a new thread and the ring sound isn't work well.
            # command += " > /dev/null 2>&1" # send the output to /dev/null

            #process1 = subprocess.Popen(command, shell=True) # detached way
            #self.fm.execute_command(command, universal_newlines=True, stdout=subprocess.PIPE) # chatgpt said that the 2nd and 3rd parameters are innecesary and cand make problems
            self.fm.execute_command(command)


    def ring_sound(self, t1):
        t1.join()
        import subprocess
        end_sound = "paplay /usr/share/sounds/freedesktop/stereo/complete.oga"
        #process2 = subprocess.Popen(end_sound, shell=True) # detached way
        self.fm.execute_command(end_sound, universal_newlines=True, stdout=subprocess.PIPE)


    def execute(self):
        from ranger.core.loader import Loader
        import threading
        t1 = threading.Thread(target=self.loop_through_all_files)
        t1.daemon = True
        t2 = threading.Thread(target=self.ring_sound, args=(t1,))
        t1.start()
        t2.start()



class flip_horizontally_an_image(Command):
    # Note: I must press enter after run the command in order to watch again ranger interface.

    def flip_image_horizontally(self, image_path, output_path):
        try:
            img = Image.open(image_path)
            flipped_img = img.transpose(Image.FLIP_LEFT_RIGHT)
            flipped_img.save(output_path)
            print(f"La imagen se ha guardado en {output_path}")
        except Exception as e:
            print(f"Error al voltear la imagen {image_path}: {e}")

    def loop_through_all_files(self):
        for index, file in enumerate(self.fm.thistab.get_selection(), start=0): 
            name_without_extension, extension = os.path.splitext(f"{file.basename}")
            image_path = f"{file.dirname}/{file.basename}"
            output_path = f"{name_without_extension}_flipped{extension}"

            self.fm.notify(f"image_path: {image_path} | output_path: {output_path}", bad=False)
            self.flip_image_horizontally(image_path, output_path)

            # command = f"ffmpeg -i {file.dirname}/'{file.basename}' -acodec libmp3lame '{name_without_extension}_audio.mp3'"
            # command = f"ffmpeg -i {this_file.dirname}/'{this_file.basename}' -acodec libmp3lame {this_file.dirname}/'{this_file.basename}.mp3' &"
            # note: I shoudn't use & at the end, because this creates a new thread and the ring sound isn't work well.
            # command += " > /dev/null 2>&1" # send the output to /dev/null

            #process1 = subprocess.Popen(command, shell=True) # detached way
            #self.fm.execute_command(command, universal_newlines=True, stdout=subprocess.PIPE) # chatgpt said that the 2nd and 3rd parameters are innecesary and cand make problems

    def ring_sound(self, t1):
        t1.join()
        import subprocess
        end_sound = "paplay /usr/share/sounds/freedesktop/stereo/complete.oga"
        #process2 = subprocess.Popen(end_sound, shell=True) # detached way
        self.fm.execute_command(end_sound, universal_newlines=True, stdout=subprocess.PIPE)

    def execute(self):
        from ranger.core.loader import Loader
        import threading
        t1 = threading.Thread(target=self.loop_through_all_files)
        t1.daemon = True
        t2 = threading.Thread(target=self.ring_sound, args=(t1,))
        t1.start()
        t2.start()
        self.fm.notify("Todas las imágenes seleccionadas han sido volteadas", bad=False)

class crop_to_854x480(Command):
    def crop_image(self, image_path, output_path):
        try:
            img = Image.open(image_path)
            width, height = img.size

            # Calcular el punto de inicio para el recorte
            # This measures cut the imagen in the center:
            # left = (width - 854) / 2
            # top = (height - 480) / 2
            # right = (width + 854) / 2
            # bottom = (height + 480) / 2

            # This measures cut the imagen in the top left:
            left = 0
            top = 0
            right = 854
            bottom = 480

            # Cortar la imagen
            cropped_img = img.crop((left, top, right, bottom))
            cropped_img.save(output_path)
            print(f"La imagen se ha guardado en {output_path}")
        except Exception as e:
            print(f"Error al cortar la imagen '{image_path}': {e}")

    def loop_through_all_files(self):
        for file in self.fm.thistab.get_selection():
            name_without_extension, extension = os.path.splitext(file.basename)
            image_path = file.path
            output_path = os.path.join(file.dirname, f"{name_without_extension}_cropped{extension}")
            print(f"Procesando: {image_path} -> {output_path}")
            self.crop_image(image_path, output_path)

    def ring_sound(self, t1):
        t1.join()
        import subprocess
        end_sound = "paplay /usr/share/sounds/freedesktop/stereo/complete.oga"
        #process2 = subprocess.Popen(end_sound, shell=True) # detached way
        self.fm.execute_command(end_sound, universal_newlines=True, stdout=subprocess.PIPE)

    def execute(self):
        from ranger.core.loader import Loader
        import threading
        t1 = threading.Thread(target=self.loop_through_all_files)
        t1.daemon = True
        t2 = threading.Thread(target=self.ring_sound, args=(t1,))
        t1.start()
        t2.start()
        self.fm.notify("Todas las imágenes seleccionadas han sido cortadas a 854x480", bad=False)



class resize_to_1280x720(Command):
    def resize_image(self, image_path, output_path):
        try:
            img = Image.open(image_path)
            # resized_img = img.resize((1280, 720), Image.ANTIALIAS) # ANTIALIAS is deprecated.
            resized_img = img.resize((1280, 720), Image.LANCZOS)

            resized_img.save(output_path)
            print(f"La imagen se ha guardado en {output_path}")
        except Exception as e:
            print(f"Error al cambiar el tamaño de la imagen '{image_path}': {e}")

    def loop_through_all_files(self):
        for file in self.fm.thistab.get_selection():
            name_without_extension, extension = os.path.splitext(file.basename)
            image_path = file.path
            output_path = os.path.join(file.dirname, f"{name_without_extension}_resized{extension}")
            print(f"Procesando: {image_path} -> {output_path}")
            self.resize_image(image_path, output_path)

    def ring_sound(self, t1):
        t1.join()
        import subprocess
        end_sound = "paplay /usr/share/sounds/freedesktop/stereo/complete.oga"
        #process2 = subprocess.Popen(end_sound, shell=True) # detached way
        self.fm.execute_command(end_sound, universal_newlines=True, stdout=subprocess.PIPE)

    def execute(self):
        from ranger.core.loader import Loader
        import threading
        t1 = threading.Thread(target=self.loop_through_all_files)
        t1.daemon = True
        t2 = threading.Thread(target=self.ring_sound, args=(t1,))
        t1.start()
        t2.start()
        self.fm.notify("Todas las imágenes seleccionadas han sido redimensionadas a 1280x720", bad=False)


class convert_from_opus_to_mp3(Command):
    # Note: I must press enter after run the command in order to watch again ranger interface.

    def loop_through_all_files(self):
        # import subprocess
        for index, file in enumerate(self.fm.thistab.get_selection(), start=0): 
            name_without_extension, _ = os.path.splitext(f"{file.basename}")

            command = f"ffmpeg -i {file.dirname}/'{file.basename}' '{name_without_extension}.mp3'"

            # note: I shoudn't use & at the end, because this creates a new thread and the ring sound isn't work well.
            command += " > /dev/null 2>&1" # send the output to /dev/null

            #process1 = subprocess.Popen(command, shell=True) # detached way
            #self.fm.execute_command(command, universal_newlines=True, stdout=subprocess.PIPE) # chatgpt said that the 2nd and 3rd parameters are innecesary and cand make problems
            self.fm.execute_command(command)


    def ring_sound(self, t1):
        t1.join()
        import subprocess
        end_sound = "paplay /usr/share/sounds/freedesktop/stereo/complete.oga"
        #process2 = subprocess.Popen(end_sound, shell=True) # detached way
        self.fm.execute_command(end_sound, universal_newlines=True, stdout=subprocess.PIPE)


    def execute(self):
        from ranger.core.loader import Loader
        import threading
        t1 = threading.Thread(target=self.loop_through_all_files)
        t1.daemon = True
        t2 = threading.Thread(target=self.ring_sound, args=(t1,))
        t1.start()
        t2.start()
        self.fm.notify("All opus files have been converted to mp3 files.", bad=False)

class convert_from_opus_to_m4a(Command):
    # Note: I must press enter after run the command in order to watch again ranger interface.

    def loop_through_all_files(self):
        # import subprocess
        for index, file in enumerate(self.fm.thistab.get_selection(), start=0): 
            name_without_extension, _ = os.path.splitext(f"{file.basename}")

            # command example: ffmpeg -i input.opus -c:a aac output.m4a
            command = f"ffmpeg -i {file.dirname}/'{file.basename}' -c:a aac '{name_without_extension}.m4a'"

            # note: I shoudn't use & at the end, because this creates a new thread and the ring sound isn't work well.
            command += " > /dev/null 2>&1" # send the output to /dev/null

            #process1 = subprocess.Popen(command, shell=True) # detached way
            #self.fm.execute_command(command, universal_newlines=True, stdout=subprocess.PIPE) # chatgpt said that the 2nd and 3rd parameters are innecesary and cand make problems
            self.fm.execute_command(command)


    def ring_sound(self, t1):
        t1.join()
        import subprocess
        end_sound = "paplay /usr/share/sounds/freedesktop/stereo/complete.oga"
        #process2 = subprocess.Popen(end_sound, shell=True) # detached way
        self.fm.execute_command(end_sound, universal_newlines=True, stdout=subprocess.PIPE)


    def execute(self):
        from ranger.core.loader import Loader
        import threading
        t1 = threading.Thread(target=self.loop_through_all_files)
        t1.daemon = True
        t2 = threading.Thread(target=self.ring_sound, args=(t1,))
        t1.start()
        t2.start()
        self.fm.notify("All opus files have been converted to .m4a files.", bad=False)

class zip_playstation_file_in_local_disk(Command):
    # Note: I must press enter after run the command in order to watch again ranger interface.

    def loop_through_all_files(self):
        # import subprocess
        for index, file in enumerate(self.fm.thistab.get_selection(), start=0): 
            name_without_extension, _ = os.path.splitext(f"{file.basename}")

            # command = f"ffmpeg -i {file.dirname}/'{file.basename}' '{name_without_extension}.mp3'"
            output_path = "/home/chalius/temp/mano-disk"
            # command = f"zip -0 -r {output_path}/{file.dirname}/{file.dirname}.zip {file.dirname}/'{file.basename}'"
            command = f"zip -0 -r '{output_path}/{file.basename}'.zip '{file.dirname}/{file.basename}'"

            # note: I shoudn't use & at the end, because this creates a new thread and the ring sound isn't work well.
            # command += " > /dev/null 2>&1" # send the output to /dev/null

            #process1 = subprocess.Popen(command, shell=True) # detached way
            #self.fm.execute_command(command, universal_newlines=True, stdout=subprocess.PIPE) # chatgpt said that the 2nd and 3rd parameters are innecesary and cand make problems
            self.fm.execute_command(command)


    def ring_sound(self, t1):
        t1.join()
        import subprocess
        end_sound = "paplay /usr/share/sounds/freedesktop/stereo/complete.oga"
        #process2 = subprocess.Popen(end_sound, shell=True) # detached way
        self.fm.execute_command(end_sound, universal_newlines=True, stdout=subprocess.PIPE)


    def execute(self):
        from ranger.core.loader import Loader
        import threading
        t1 = threading.Thread(target=self.loop_through_all_files)
        t1.daemon = True
        t2 = threading.Thread(target=self.ring_sound, args=(t1,))
        t1.start()
        t2.start()
        self.fm.notify("Convert to zip and copy to the desired output path.", bad=False)

class split_file_in_1G_size_files(Command):
    # Note: I must press enter after run the command in order to watch again ranger interface.

    def loop_through_all_files(self):
        # import subprocess
        for index, file in enumerate(self.fm.thistab.get_selection(), start=0): 
            name_without_extension, _ = os.path.splitext(f"{file.basename}")

            command = f"mkdir '{name_without_extension}' && split -b 1G -d --additional-suffix=.zip '{file.dirname}/{file.basename}' './{name_without_extension}/{name_without_extension}_part_'"

            # note: I shoudn't use & at the end, because this creates a new thread and the ring sound isn't work well.
            command += " > /dev/null 2>&1" # send the output to /dev/null

            #process1 = subprocess.Popen(command, shell=True) # detached way
            #self.fm.execute_command(command, universal_newlines=True, stdout=subprocess.PIPE) # chatgpt said that the 2nd and 3rd parameters are innecesary and cand make problems
            self.fm.execute_command(command)

    def ring_sound(self, t1):
        t1.join()
        import subprocess
        end_sound = "paplay /usr/share/sounds/freedesktop/stereo/complete.oga"
        #process2 = subprocess.Popen(end_sound, shell=True) # detached way
        self.fm.execute_command(end_sound, universal_newlines=True, stdout=subprocess.PIPE)


    def execute(self):
        from ranger.core.loader import Loader
        import threading
        t1 = threading.Thread(target=self.loop_through_all_files)
        t1.daemon = True
        t2 = threading.Thread(target=self.ring_sound, args=(t1,))
        t1.start()
        t2.start()
        self.fm.notify("Split zip file in 1G small zip files.", bad=False)

class add_name_text_to_image(Command):
    """
        When I upload pictures to telegram the name and the date are removed,
        so I use this script to put the picture name(which has the date) in the picture.
    """


    def __add_text_to_image(self, image_path, output_path, text, font_path=None, font_size=55):
        import platform
        try:
            # Open the image
            image = Image.open(image_path)
            draw = ImageDraw.Draw(image)

            # Load a font
            font_path_default = ""
            if platform.system() == "Windows":
                font_path_default = r"C:\Windows\Fonts\impact.ttf"  # for windows
            elif platform.system() == "Linux":
                # font_path_default = "/home/chalius/.local/share/fonts/ttf/Impact/impact.ttf"  # for linux
                font_path_default = "/home/chalius/.local/share/fonts/ttf/nerdfonts/Agave/AgaveNerdFont-Regular.ttf"  # for linux

            # font = ImageFont.truetype(font_path, font_size) if font_path else ImageFont.load_default()
            font = ImageFont.truetype(font_path, font_size) if font_path else ImageFont.truetype(font_path_default, font_size)

            # Calculate text size and position
            ascent, descent = font.getmetrics()
            text_height = ascent + descent
            # text_width = draw.textlength(text, font=font)
            x = 10  # 10 pixels from the left
            y = image.height - text_height - 10  # 10 pixels from the bottom

            # Add text to the image
            draw.text((x, y), text, font=font, fill=(255, 0, 0))  # white text

            # Save the edited image
            image.save(output_path)

            self.fm.notify(f"Saved image with text '{text}' to {output_path}", bad=False)
        except Exception as e:
            self.fm.notify(f"Error al cambiar el tamaño de la imagen '{image_path}': {e}", bad=True)

    def loop_through_all_files(self):
        # import subprocess
        for index, file in enumerate(self.fm.thistab.get_selection(), start=0): 
            # name_without_extension, _ = os.path.splitext(f"{file.basename}")
            if file.basename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
                image_path = os.path.join(file.dirname, file.basename)
                output_path = os.path.join(file.dirname, f"annotated_{file.basename}")
                self.__add_text_to_image(image_path, output_path, file.basename)

    def ring_sound(self, t1):
        t1.join()
        import subprocess
        end_sound = "paplay /usr/share/sounds/freedesktop/stereo/complete.oga"
        #process2 = subprocess.Popen(end_sound, shell=True) # detached way
        self.fm.execute_command(end_sound, universal_newlines=True, stdout=subprocess.PIPE)


    def execute(self):
        # from ranger.core.loader import Loader
        import threading
        t1 = threading.Thread(target=self.loop_through_all_files)
        t1.daemon = True
        t2 = threading.Thread(target=self.ring_sound, args=(t1,))
        t1.start()
        t2.start()
        # self.fm.notify("added the name to the image", bad=False)

class convert_pdf_to_jpeg(Command):
    """
    This command uses pdftoppm linux command.
        - NOTE: this command has an little error, I must press <enter> after I sended the command.
    """

    def loop_through_all_files(self):
        # import subprocess
        for index, file in enumerate(self.fm.thistab.get_selection(), start=0): 
            name_without_extension, _ = os.path.splitext(f"{file.basename}")

            # command example: ffmpeg -i input.opus -c:a aac output.m4a
            # command = f"pdftoppm {file.dirname}/'{file.basename}' '{name_without_extension}.jpeg' -jpeg"
            command = f"pdftoppm {file.dirname}/'{file.basename}' {file.dirname}/'{name_without_extension}' -jpeg"
            # command that works: pdftoppm nov-2024.pdf nov-2024.jpeg -jpeg

            # self.fm.notify(f"pdftoppm {file.dirname}/'{file.basename}' {file.dirname}/'{name_without_extension}.jpeg' -jpeg", bad=False)

            # note: I shoudn't use & at the end, because this creates a new thread and the ring sound isn't work well.
            command += " > /dev/null 2>&1" # send the output to /dev/null

            self.fm.execute_command(command)


    def ring_sound(self, t1):
        t1.join()
        import subprocess
        end_sound = "paplay /usr/share/sounds/freedesktop/stereo/complete.oga"
        #process2 = subprocess.Popen(end_sound, shell=True) # detached way
        self.fm.execute_command(end_sound, universal_newlines=True, stdout=subprocess.PIPE)


    def execute(self):
        from ranger.core.loader import Loader
        import threading
        t1 = threading.Thread(target=self.loop_through_all_files)
        t1.daemon = True
        t2 = threading.Thread(target=self.ring_sound, args=(t1,))
        t1.start()
        t2.start()
        self.fm.notify("The pdf file was convert to jpeg.", bad=False)
