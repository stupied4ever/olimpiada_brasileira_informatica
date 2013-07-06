require 'spec_helper'

describe 'AutoCorretor' do
  subject(:auto_corretor) { AutoCorretor.new }

  describe '#distancia' do
    subject { auto_corretor.distancia(de, ate) }
    let(:de)  { 'rafael' }

    context 'com duas palavras iguais' do
      let(:ate) { 'rafael' }

      it { should eq(0) }
    end

     context 'com segunda palavra faltando uma letra no fim' do
       let(:ate) { 'rafae' }

       it { should eq(1) }
     end

    context 'com segunda palavra faltando uma letra no inicio' do
      let(:ate) { 'afael' }

      it { should eq(1) }
    end

    context 'com segunda palavra faltando duas letras no inicio' do
      let(:ate) { 'fael' }

      it { should eq(2) }
    end

    context 'com segunda palavra faltando todas as letras' do
      let(:ate) { '' }

      it { should eq(6) }
    end
  end
end
