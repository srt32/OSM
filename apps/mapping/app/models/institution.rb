class Institution < ActiveRecord::Base
  attr_accessible :gmaps, :id, :latitude, :longitude, :title

  geocoded_by :address
  after_validation :geocode, :if => :title_changed?

  acts_as_gmappable

  def gmaps4rails_address
  	"#{self.address}"
  end

  def address
  	[title].compact.join(', ')
  end
end
