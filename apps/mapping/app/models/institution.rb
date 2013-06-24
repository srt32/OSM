class Institution < ActiveRecord::Base
  attr_accessible :gmaps, :id, :latitude, :longitude, :title
end
