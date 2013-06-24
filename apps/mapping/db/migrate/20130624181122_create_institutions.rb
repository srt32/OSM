class CreateInstitutions < ActiveRecord::Migration
  def self.up
    create_table :institutions do |t|
      t.integer :id
      t.string :title
      t.float :latitude
      t.float :longitude
      t.boolean :gmaps

      t.timestamps
    end
  end

  def self.down
    drop_table :institutions
  end
end
