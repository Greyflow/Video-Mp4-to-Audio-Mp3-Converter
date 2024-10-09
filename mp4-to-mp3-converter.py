import os
from moviepy.editor import VideoFileClip

def get_input():
    while True:
        file_path = input("Enter the path to the MP4 file: ")
        if os.path.isfile(file_path) and file_path.lower().endswith('.mp4'):
            return file_path
        else:
            print("Invalid file path or not an MP4 file. Please try again.")

def check_file_format(file_path):
    _, extension = os.path.splitext(file_path)
    if extension.lower() != '.mp4':
        raise ValueError("The input file is not in MP4 format.")

def extract_audio_and_save(input_path, output_path):
    video = VideoFileClip(input_path)
    audio = video.audio
    audio.write_audiofile(output_path)
    audio.close()
    video.close()

def main():
    print("MP4 to MP3 Converter")
    
    # Get input
    input_file = get_input()
    
    try:
        # Check file format
        check_file_format(input_file)
        
        # Generate output file name
        output_file = os.path.splitext(input_file)[0] + '.mp3'
        
        # Extract audio and save as MP3
        print("Converting MP4 to MP3...")
        extract_audio_and_save(input_file, output_file)
        
        # Output
        print(f"Conversion complete. MP3 file saved as: {output_file}")
    
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
