class Datapoint < ActiveRecord::Base
  attr_accessible :gmaps, :latitude, :longitude, :name

  acts_as_gmappable

  def gmaps4rails_address
  	#
  end
end
