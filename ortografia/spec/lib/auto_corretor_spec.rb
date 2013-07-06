require 'spec_helper'

describe 'AutoCorretor' do
  subject(:auto_corretor) { AutoCorretor.new }

  describe '#distancia' do
    subject { auto_corretor.distancia(de, ate) }

    context 'com duas palavras iguais' do
      let(:de)  { 'rafael' }
      let(:ate) { 'rafael' }

      it { should eq(0) }
    end
  end
end
