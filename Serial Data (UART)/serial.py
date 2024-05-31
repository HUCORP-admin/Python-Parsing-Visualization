import os
import pandas as pd
import matplotlib.pyplot as plt
from parsers import parse_serial


def extract_zmod_data(dfs):
    iaq, tvoc, co2 = [], [], []
    for df in dfs:
        iaq.append(df.loc[(df['sensor'] == 'ZMOD4410') & (df['reading'] == 'IAQ')])
        tvoc.append(df.loc[(df['sensor'] == 'ZMOD4410') & (df['reading'] == 'TVOC')])
        co2.append(df.loc[(df['sensor'] == 'ZMOD4410') & (df['reading'] == 'CO2')])

    return iaq, tvoc, co2

def extract_scd_data(dfs):
    t, rh, co2 = [], [], []
    for df in dfs:
        t.append(df.loc[(df['sensor'] == 'SCD41') & (df['reading'] == 'T')])
        rh.append(df.loc[(df['sensor'] == 'SCD41') & (df['reading'] == 'RH')])
        co2.append(df.loc[(df['sensor'] == 'SCD41') & (df['reading'] == 'CO2')])

    return t, rh, co2

def extract_bme_data(dfs):
    t, p, co2, rh, ct, ch, siaq, iaq, rg, bvoc = [], [], [], [], [], [], [], [], [], []
    for df in dfs:
        t.append(df.loc[(df['sensor'] == 'BME688') & (df['reading'] == 'T')])
        p.append(df.loc[(df['sensor'] == 'BME688') & (df['reading'] == 'P')])
        co2.append(df.loc[(df['sensor'] == 'BME688') & (df['reading'] == 'CO2')])
        rh.append(df.loc[(df['sensor'] == 'BME688') & (df['reading'] == 'RH')])
        ct.append(df.loc[(df['sensor'] == 'BME688') & (df['reading'] == 'CT')])
        ch.append(df.loc[(df['sensor'] == 'BME688') & (df['reading'] == 'CH')])
        siaq.append(df.loc[(df['sensor'] == 'BME688') & (df['reading'] == 'SIAQ')])
        iaq.append(df.loc[(df['sensor'] == 'BME688') & (df['reading'] == 'IAQ')])
        rg.append(df.loc[(df['sensor'] == 'BME688') & (df['reading'] == 'RG')])
        bvoc.append(df.loc[(df['sensor'] == 'BME688') & (df['reading'] == 'BVOC')])

    return t, p, co2, rh, ct, ch, siaq, iaq, rg, bvoc

def plot_zmod(n, iaq, tvoc, co2):
    # prepare figure
    fig, axs = plt.subplots(3, sharex=True, figsize=(7,9))
    fig.suptitle('ZMOD4410 Readings')
    plt.subplots_adjust(top=0.94, bottom=0.06)

    # plot data
    for i in range(n):
        iaq[i].plot(x='time', y='value', xlabel='Time (s)', ylabel='IAQ', ax=axs[0], xlim=[0, 40000], label=f'COM{i+3}').legend(loc='upper right')
        tvoc[i].plot(x='time', y='value', xlabel='Time (s)', ylabel='TVOC', ax=axs[1], xlim=[0, 40000], label=f'COM{i+3}').legend(loc='upper right')
        co2[i].plot(x='time', y='value', xlabel='Time (s)', ylabel='CO2', ax=axs[2], xlim=[0, 40000], label=f'COM{i+3}').legend(loc='upper right')

def plot_scd(n, t, rh, co2):
    # prepare figure
    fig, axs = plt.subplots(3, sharex=True, figsize=(7,9))
    fig.suptitle('SCD41 Readings')
    plt.subplots_adjust(top=0.94, bottom=0.06)

    # plot data
    for i in range(n):
        t[i].plot(x='time', y='value', xlabel='Time (s)', ylabel='T', ax=axs[0], xlim=[0, 40000], label=f'COM{i+3}').legend(loc='upper right')
        rh[i].plot(x='time', y='value', xlabel='Time (s)', ylabel='RH', ax=axs[1], xlim=[0, 40000], label=f'COM{i+3}').legend(loc='upper right')
        co2[i].plot(x='time', y='value', xlabel='Time (s)', ylabel='CO2', ax=axs[2], xlim=[0, 40000], label=f'COM{i+3}').legend(loc='upper right')

def plot_bme(n, t, p, co2, rh, ct, ch, siaq, iaq, rg, bvoc):
    # prepare figure
    fig, axs = plt.subplots(2, 5, sharex=True, figsize=(17,9))
    fig.suptitle('BME688 Readings')
    fig.tight_layout(w_pad=3.0)
    plt.subplots_adjust(left=0.04, right=.96, top=0.94, bottom=0.06)
    axs[0,2].ticklabel_format(axis='y', style='sci', scilimits=(0,0))
    axs[1,3].ticklabel_format(axis='y', style='sci', scilimits=(0,0))

    # plot data
    for i in range(n):
        t[i].plot(x='time', y='value', xlabel='Time (s)', ylabel='T', ax=axs[0,0], xlim=[0, 40000], label=f'COM{i+3}').legend(loc='upper right')
        p[i].plot(x='time', y='value', xlabel='Time (s)', ylabel='P', ax=axs[0,1], xlim=[0, 40000], label=f'COM{i+3}').legend(loc='upper right')
        co2[i].plot(x='time', y='value', xlabel='Time (s)', ylabel='CO2', ax=axs[0,2], xlim=[0, 40000], label=f'COM{i+3}').legend(loc='upper right')
        rh[i].plot(x='time', y='value', xlabel='Time (s)', ylabel='RH', ax=axs[0,3], xlim=[0, 40000], label=f'COM{i+3}').legend(loc='upper right')
        ct[i].plot(x='time', y='value', xlabel='Time (s)', ylabel='CT', ax=axs[0,4], xlim=[0, 40000], label=f'COM{i+3}').legend(loc='upper right')
        ch[i].plot(x='time', y='value', xlabel='Time (s)', ylabel='CH', ax=axs[1,0], xlim=[0, 40000], label=f'COM{i+3}').legend(loc='upper right')
        siaq[i].plot(x='time', y='value', xlabel='Time (s)', ylabel='SIAQ', ax=axs[1,1], xlim=[0, 40000], label=f'COM{i+3}').legend(loc='upper right')
        iaq[i].plot(x='time', y='value', xlabel='Time (s)', ylabel='IAQ', ax=axs[1,2], xlim=[0, 40000], label=f'COM{i+3}').legend(loc='upper right')
        rg[i].plot(x='time', y='value', xlabel='Time (s)', ylabel='RG', ax=axs[1,3], xlim=[0, 40000], label=f'COM{i+3}').legend(loc='upper right')
        bvoc[i].plot(x='time', y='value', xlabel='Time (s)', ylabel='BVOC', ax=axs[1,4], xlim=[0, 40000], label=f'COM{i+3}').legend(loc='upper right')


if __name__ == '__main__':
    LOGS_DIR = 'logs\serial'
    dfs = []

    for idx, file in enumerate(os.listdir(LOGS_DIR)):
        print(f'Parsing file {idx}...')
        f = os.path.join(LOGS_DIR, file)

        if os.path.isfile(f):
            result = parse_serial(f)
            df = pd.DataFrame(result)
            dfs.append(df)

    n_devices = len(dfs)

    # extract data from dataframes
    zmod_iaq, zmod_tvoc, zmod_co2 = extract_zmod_data(dfs)
    scd_t, scd_rh, scd_co2 = extract_scd_data(dfs)
    bme_t, bme_p, bme_co2, bme_rh, bme_ct, bme_ch, bme_siaq, bme_iaq, bme_rg, bme_bvoc = extract_bme_data(dfs)

    # plot figures
    plot_zmod(n_devices, zmod_iaq, zmod_tvoc, zmod_co2)
    plot_scd(n_devices, scd_t, scd_rh, scd_co2)
    plot_bme(n_devices, bme_t, bme_p, bme_co2, bme_rh, bme_ct, bme_ch, bme_siaq, bme_iaq, bme_rg, bme_bvoc)

    plt.show()
