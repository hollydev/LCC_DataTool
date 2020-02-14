# coding: utf-8
import spikes.Fuzzy.fw_matcher as match
import source.getFiles as read
files = read.get_files("../../D2L Data/")[1:500]
frames = read.get_data_frames(files)
frame = read.concat_data_frames(frames)
filt_frame = frame[frame["GradeItemName"].notnull()]
match.clean(filt_frame.GradeItemName)
