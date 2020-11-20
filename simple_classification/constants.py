from pathlib import Path
'''
TEST_LIST = ['Bach.french-suite_bwv812_no1_allemande.mm_1-end.s004',
             'Bach.french-suite_bwv816_no5_courante.mm_1-end.s002',
             'Chopin.nocturne_op9_no2_.mm_1-12.s021',
             'Schumann.fantasiestucke_op12_no3_.mm_1-42.s021',
             'Bach.minuet_bwv114__.mm_1-32.s018',
             'Schubert.impromptu_op142_no3_var1.mm_1-end.s018',
             'Schubert.impromptu_op142_no3_thema.mm_1-end.s018',
             'Schumann.symphonicetudes_op.13_thema.mm_1-end.s018',
             'Chopin.waltz_op69_no1_.mm_1-16.s020',
             'Bach.minuet_bwv114__.mm_1-32.s016',
             'Schumann.kinderszenen_op15_no7_traumerei.mm_1-end.s014',
             'Schumann.davidsbundlertanze_op6_no2_.mm_1-end.s015',
             'Bartok.roumanian-folk-dances_sz56_no3_.mm_1-end.s005',
             'Bartok.roumanian-folk-dances_sz56_no4_.mm_1-end.s005',
             'Bach.prelude-and-fugue_bwv875_no6_prelude.mm_1-end.s022',
             'Rachmaninoff.piano-concerto_op18_no2_mov1.mm_83-103.s022',
             'Chopin.prelude_op28_no4_.mm_1-12.s007',
             'Beethoven.sonata_op31-2_no17_mov2.mm_1-17.s007',
             'Chopin.valse-brillante_op34_no2_.mm_1-36.s007',
             'Chopin.nocturne_op9_no2_.mm_1-12.s007',
             'Liszt.consolation_s172_no3_.mm_1-45.s007',
             'Mozart.sonata_k545_no16_mov3.mm_1-20.s007',
             'Mozart.sonata_k332_no12_mov2.mm_1-8.s007',
             'Beethoven.sonata_op57_no23_mov3.mm_1-67.s007',
             'Chopin.etude_op25_no7_.mm_1-20.s007',
             'Schumann.kinderszenen_op15_no7_traumerei.mm_1-end.s007',
             'Bach.prelude-and-fugue_bwv880_no11_prelude.mm_1-end.s006',
             'Rachmaninoff.sonata_op36_no2_mov1.mm_1-37.s011',
             'Clementi.sonatine_op36_no1_mov2.mm_1-end.s012',
             'Chopin.valse-brillante_op34_no2_.mm_1-36.s008',
             'Chopin.etude_op10_no4_.mm_1-33.s013']

VALID_LIST = ['Bach.french-suite_bwv816_no5_gavotte.mm_1-end.s002',
              'Bach.french-suite_bwv816_no5_gigue.mm_1-end.s002',
              'Bach.partita_bwv825_no1_minuet1-2.mm_1-end.s018',
              'Bach.prelude-and-fugue_bwv883_no14_prelude.mm_1-end.s018',
              'Prokofiev.sonata_op14_no2_mov1.mm_1-127.s018',
              'Schubert.impromptu_op142_no3_var3.mm_1-16.s018',
              'Bach.prelude-and-fugue_bwv870_no1_prelude.mm_1-19.s007',
              'Beethoven.sonata_op31-2_no17_mov3.mm_1-43.s007',
              'Mozart.sonata_k545_no16_mov2.mm_1-16.s007',
              'Bartok.roumanian-folk-dances_sz56_no2_.mm_1-end.s005',
              'Bartok.roumanian-folk-dances_sz56_no5_.mm_1-end.s005',
              'Beethoven.sonata_op10-3_no7_mov1.mm_1-125.s011',
              'Mozart.nine-variations-on-a-lison-dormait_k573__.mm_1-72.s011'
              'Rachmaninoff.sonata_op36_no2_mov2.mm_1-23.s011',
              'Chopin.barcarolle_op60__.mm_1-38.s019',
              'Beethoven.sonata_op27-2_no14_mov1.mm_1-23.s008',
              'Chopin.berceuse_op57__.mm_1-34.s017',
              'Chopin.nocturne_op48_no1_.mm_1-24.s004',
              'Schumann.davidsbundlertanze_op6_no14_.mm_1-end.s015',
              'Schumann.davidsbundlertanze_op6_no18_.mm_1-end.s015',
              'Schumann.davidsbundlertanze_op6_no5_.mm_1-end.s015',
              'Liszt.dante-sonata_s161_no7_.mm_35-54.s022',
              'Mompou.cancion-y-danza__no6_cancion.mm_1-end.s022',
              'Chopin.waltz_op69_no2_.mm_1-16.s012',
              'Beethoven.sonata_op109_no30_mov1.mm_1-59.s019',
              'Schubert.sonata_d850_no17_mov1.mm_1-47.s019',
              'Chopin.etude_op25_no9_.mm_1-37.s013',
              'Mozart.sonata_k332_no12_mov1.mm_1-40.s007']
'''

FEATURE_KEYS = ['beat_tempo_ratio_mean',
                'beat_tempo_ratio_std',
                'relative_beat_tempo_mean',

                'velocity_ratio_mean',
                'velocity_ratio_std',
                'relative_velocity_mean',
                'relative_velocity_std',
                'relative_velocity_kurt',

                'original_duration_ratio_mean',
                'relative_original_duration_mean']

STAT_TYPE = 'scaled_statistics'

BATCH_SIZE = 1
NUM_EPOCH = 67
LEARNING_RATE = 1e-3

TEST_LIST_20 = ['Bach.french-suite_bwv816_no5_gavotte.mm_1-end.s002', 'Bach.toccata_bwv914__.mm_14-41.s007', 'Bach.prelude-and-fugue_bwv870_no1_fugue.mm_1-46.s007', 'Bach.inventions_bwv775_no4_.mm_1-end.s020', 'Scarlatti.sonata_k481__.mm_1-35.s018', 'Bach.french-suite_bwv816_no5_courante.mm_1-end.s002', 'Bach.french-suite_bwv816_no5_allemande.mm_1-12.s021', 'Mozart.sonata_k331_no11_mov3.mm_1-32.s016', 'Beethoven.sonata_op13_no8_mov3.mm_1-43.s007', 'Hanon.the-virtuoso-pianist__no39_cmajor.mm_1-end.s018', 'Beethoven.sonata_op109_no30_mov3.mm_1-67.s019', 'Beethoven.sonata_op110_no31_mov2.mm_1-96.s018', 'Beethoven.sonata_op13_no8_mov3.mm_104-120.s007', 'Beethoven.sonata_op57_no23_mov2.mm_1-32.s007', 'Beethoven.sonata_op57_no23_mov3.mm_1-67.s007', 'Beethoven.sonata_op110_no31_mov1.mm_1-40.s006', 'Beethoven.sonata_op110_no31_mov3.mm_27-110.s018', 'Beethoven.sonata_op57_no23_mov1.mm_35-50.s007', 'Mozart.sonata_k545_no16_mov3.mm_1-20.s007', 'Mozart.sonata_k331_no11_mov3.mm_1-41.s020', 'Mozart.sonata_k545_no16_mov2.mm_1-16.s007', 'Chopin.nocturne_opposth_no20_.mm_21-46.s007',
                'Schubert.impromptu_op90_no2_.mm_1-51.s007', 'Schumann.fantasiestucke_op12_no1_.mm_1-16.s021', 'Chopin.andante-spianato-et-grand-polonaise-brillante_op22__.mm_1-36.s014', 'Chopin.mazurka_op7_no1_.mm_1-24.s022', 'Scriabin.sonata_op19_no2_mov1.mm_1-58.s018', 'Mendelssohn.capriccio_op33_no1_.mm_15-59.s007', 'Schubert.impromptu_op142_no3_thema.mm_1-end.s018', 'Chopin.nocturne_opposth_no20_.mm_1-20.s007', 'Mendelssohn.variations-serieuses_op54__.mm_1-98.s019', 'Chopin.andante-spianato-et-grand-polonaise-brillante_op22__.mm_1-end.s005', 'Chopin.etude_op25_no7_.mm_1-20.s007', 'Chopin.mazurka_op24_no1_.mm_1-32.s015', 'Debussy.ballade_l78__.mm_88-end.s022', 'Rachmaninoff.sonata_op36_no2_mov2.mm_1-23.s011', 'Schumann.davidsbundlertanze_op6_no14_.mm_1-end.s015', 'Chopin.etude_op10_no3_.mm_1-21.s007', 'Chopin.nocturne_op27-2_no8_.mm_1-9.s013', 'Schumann.davidsbundlertanze_op6_no2_.mm_1-end.s015', 'Mendelssohn.capriccio_op33_no1_.mm_61-84.s007', 'Prokofiev.sonata_op14_no2_mov2.mm_1-end.s018', 'Bartok.roumanian-folk-dances_sz56_no6_.mm_1-end.s005']
TEST_LIST_30 = ['Bach.french-suite_bwv816_no5_sarabande.mm_1-16.s021', 'Bach.french-suite_bwv816_no5_sarabande.mm_1-end.s002', 'Bach.french-suite_bwv816_no5_allemande.mm_1-12.s021', 'Bach.french-suite_bwv816_no5_bourree.mm_1-end.s002', 'Bach.prelude-and-fugue_bwv875_no6_prelude.mm_1-end.s022', 'Bach.prelude-and-fugue_bwv883_no14_prelude.mm_1-end.s018', 'Bach.french-suite_bwv812_no1_allemande.mm_1-end.s004', 'Bach.prelude-and-fugue_bwv870_no1_prelude.mm_1-19.s007', 'Bach.french-suite_bwv816_no5_gavotte.mm_1-end.s002', 'Bach.toccata_bwv914__.mm_42-70.s007', 'Bach.french-suite_bwv816_no5_allemande.mm_1-12.s002', 'Mozart.sonata_k545_no16_mov3.mm_1-20.s007', 'Mozart.sonata_k331_no11_mov3.mm_1-32.s016', 'Beethoven.sonata_op31-2_no17_mov3.mm_1-43.s007', 'Mozart.nine-variations-on-a-minuet-by-Duport_k573__.mm_1-72.s011', 'Beethoven.sonata_op31-2_no17_mov2.mm_1-17.s007', 'Beethoven.sonata_op13_no8_mov3.mm_79-103.s007', 'Mozart.fantasia_k397_no3_.mm_1-34.s006', 'Beethoven.sonata_op110_no31_mov3.mm_27-110.s018', 'Beethoven.sonata_op109_no30_mov1.mm_1-59.s019', 'Mozart.sonata_k332_no12_mov1.mm_1-40.s007', 'Beethoven.sonata_op57_no23_mov2.mm_1-32.s007', 'Mozart.sonata_k332_no12_mov2.mm_1-8.s007', 'Beethoven.sonata_op57_no23_mov1.mm_1-16.s007', 'Beethoven.bagatelle_woo59_no25_.mm_1-41.s016', 'Mozart.sonata_k331_no11_mov3.mm_1-41.s020', 'Beethoven.sonata_op27-2_no14_mov1.mm_1-23.s008', 'Beethoven.sonata_op109_no30_mov3.mm_1-67.s019', 'Beethoven.sonata_op110_no31_mov1.mm_1-40.s006', 'Beethoven.sonata_op110_no31_mov1.mm_1-56.s018', 'Beethoven.sonata_op10-3_no7_mov1.mm_1-125.s011', 'Beethoven.sonata_op57_no23_mov3.mm_1-67.s007',
                'Hanon.the-virtuoso-pianist__no39_cmajor.mm_1-end.s018', 'Chopin.etude_op10_no4_.mm_1-33.s013', 'Chopin.prelude_op28_no15_.mm_28-75.s007', 'Mendelssohn.capriccio_op33_no1_.mm_1-14.s007', 'Schubert.impromptu_op90_no2_.mm_1-51.s007', 'Schumann.fantasiestucke_op12_no1_.mm_1-16.s021', 'Chopin.mazurka_op24_no1_.mm_1-32.s015', 'Chopin.nocturne_opposth_no20_.mm_1-20.s007', 'Schumann.fantasiestucke_op12_no1_.mm_55-88.s021', 'Schubert.impromptu_op142_no3_thema.mm_1-end.s018', 'Chopin.nocturne_opposth_no20_.mm_21-46.s007', 'Chopin.fantaisie_op49__.mm_1-42.s004', 'Schumann.kinderszenen_op15_no7_traumerei.mm_1-end.s014', 'Rachmaninoff.sonata_op36_no2_mov1.mm_1-37.s011', 'Chopin.etude_op10_no8_.mm_1-30.s014', 'Chopin.mazurka_op7_no1_.mm_1-24.s022', 'Schumann.symphonic_etudes_op13_thema.mm_1-end.s018', 'Chopin.etude_op10_no6_.mm_1-end.s007', 'Chopin.waltz_op69_no2_.mm_1-16.s012', 'Chopin.fantasie-impromptu_op66_no4_.mm_1-25.s016', 'Schumann.davidsbundlertanze_op6_no11_.mm_1-end.s015', 'Chopin.mazurka_op17_no4_.mm_61-end.s003', 'Chopin.nocturne_op27-2_no8_.mm_14-26.s013', 'Chopin.nocturne_op15_no3_.mm_1-88.s003', 'Mendelssohn.variations-serieuses_op54__.mm_1-98.s019', 'Mendelssohn.capriccio_op33_no1_.mm_15-59.s007', 'Chopin.etude_op25_no9_.mm_1-37.s013', 'Schubert.impromptu_op90_no2_.mm_83-126.s007', 'Chopin.prelude_op28_no15_.mm_1-27.s007', 'Schumann.fantasiestucke_op12_no3_.mm_1-42.s021', 'Schumann.davidsbundlertanze_op6_no18_.mm_1-end.s015', 'Chopin.nocturne_op15_no3_.mm_89-end.s003', 'Bartok.roumanian-folk-dances_sz56_no6_.mm_1-end.s005', 'Prokofiev.sonata_op14_no2_mov2.mm_1-end.s018', 'Bartok.roumanian-folk-dances_sz56_no3_.mm_1-end.s005']
