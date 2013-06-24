#lib/tasks/imports.rake
# to call, bundle exec rake imports
# HARDCODED
require 'csv'
  desc "Imports a CSV file into an ActiveRecord table"
  task :imports, [:filename] => :environment do
    CSV.foreach('schoolsLL.csv', :headers => true) do |row|
      Institution.create!(row.to_hash)
    end
  end