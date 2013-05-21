#!/bin/env ruby
# encoding: utf-8

# http://erikonrails.snowedin.net/?p=212
# to call rake csv_model_import[bunnies.csv,Datapoint]

#lib/tasks/import.rake
# desc “Imports a CSV file into an ActiveRecord table”
task :csv_model_import, [:filename, :model] => [:environment] do |task,args|
  lines = File.new(args[:filename]).readlines
  header = lines.shift.strip
  keys = header.split(',')
  lines.each do |line|
  myModel = Module.const_get(args[:model]).new
    values = line.strip.split(',')
    keys.each_with_index do |key,i|
      myModel.send("#{key.strip}=", values[i].strip) unless values[i].nil?
    end
   myModel.save
end
end