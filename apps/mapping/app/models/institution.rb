class Institution < ActiveRecord::Base
  attr_accessible :gmaps, :id, :latitude, :longitude, :title

  acts_as_gmappable

  def gmaps4rails_address
  	#
  end
end
