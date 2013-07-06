require 'spec_helper'

describe 'AutoCorretor' do
  subject(:auto_corretor) { AutoCorretor.new }

  describe '#distancia' do
    subject { auto_corretor.distancia(de, ate) }
    let(:de)  { 'rafael' }

    context 'com segunda palavra faltando uma letra' do
      let(:ate) { 'afael' }

      it { should eq(1) }
    end

    context 'com duas palavras iguais' do
      let(:ate) { 'rafael' }

      it { should eq(0) }
    end
  end
end
